import hashlib, binascii, os
import random as rdm
from datetime import datetime
import subprocess

def hash_pass( password ):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)

def verify_pass(provided_password, stored_password):
    """Verify a stored password against one provided by user"""
    stored_password = stored_password.decode('ascii')
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def serialData (data):
    return (data - datetime(1899, 12, 30).date()).days


# def getLastCommitCode():
#     try:
#         # Execute o comando Git e capture a saída
#         output = subprocess.check_output(['git', 'log', '-1', '--pretty=format:%h'], text=True)
        
#         # Retorna os 10 primeiros caracteres do hash do último commit
#         return output.strip()[:10]
#     except subprocess.CalledProcessError as e:
#         # Lida com erros, se houver
#         print(f"Erro ao executar o comando Git: {e}")
#         return None