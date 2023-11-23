from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from util import hash_pass, verify_pass
import json
app = Flask(__name__)

@app.route('/main')
def index():
    return render_template('index.html', status=None)

@app.route('/submit', methods=['POST'])
def submit():
    valor = request.form.get('valor')
    evento = request.form.get('evento')
    pwd = request.form.get('token')
    dia = request.form.get('dia')
    pagamento = request.form.get('pagamento')
    data = datetime.strptime(dia, "%d/%m/%Y").date()
    dataString = data.strftime("%d/%m/%Y")

    # Configuração do google sheets
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
    client = gspread.authorize(creds)

    # Abrir a planilha e selecionar a guia
    spreadsheet = client.open('Gastos')
    worksheet = spreadsheet.worksheet('Nov')

    
    with open('token.json', 'r') as file:
        pwdAutenticated = json.load(file)
    encodedPwd = hash_pass(pwdAutenticated['pwd'])

    if verify_pass(pwd, encodedPwd):
        worksheet.append_row([float(valor), evento, dataString, pagamento])
        return render_template('index.html', status='success')
    else:
        return render_template('index.html', status='error')
    
if __name__ == '__main__':
    app.run(debug=True)
