from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from util import hash_pass, verify_pass, serialData
import json
app = Flask(__name__)

meses = [
    {'nome': 'Jan', 'valor': 1},
    {'nome': 'Fev', 'valor': 2},
    {'nome': 'Mar', 'valor': 3},
    {'nome': 'Abr', 'valor': 4},
    {'nome': 'Mai', 'valor': 5},
    {'nome': 'Jun', 'valor': 6},
    {'nome': 'Jul', 'valor': 7},
    {'nome': 'Ago', 'valor': 8},
    {'nome': 'Set', 'valor': 9},
    {'nome': 'Out', 'valor': 10},
    {'nome': 'Nov', 'valor': 11},
    {'nome': 'Dez', 'valor': 12}
]
mesAtual = datetime.today().month
for mes in meses:
    if mes['valor'] == mesAtual:
        worksheetCorrespondente = mes['nome']
        break

@app.route('/')
def root():
    return redirect('/main')

@app.route('/main')
def index():
    # commitCode = getLastCommitCode()
    # if commitCode is not None:
    #     print(f"Último commit: {commitCode}")
    # else:
    #     print("Não foi possível obter informações do último commit.")
    # return render_template('index.html', status=None, commitVersion=commitCode)
    return render_template('index.html', status=None)

@app.route('/submit', methods=['POST'])
def submit():
    valor = request.form.get('valor')
    valorTratado = valor.replace(",", ".")
    valorTratado = float(valorTratado)
    valor=valorTratado
    evento = request.form.get('evento')
    pwd = request.form.get('token')
    dia = request.form.get('dia')
    pagamento = request.form.get('pagamento')
    data = datetime.strptime(dia, "%d/%m/%Y").date()
    dataSerial = serialData(data)

    # Configuração do google sheets
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
    client = gspread.authorize(creds)

    # Abrir a planilha e selecionar a guia
    spreadsheet = client.open('Gastos')
    worksheet = spreadsheet.worksheet(worksheetCorrespondente)

    
    with open('token.json', 'r') as file:
        pwdAutenticated = json.load(file)
    encodedPwd = hash_pass(pwdAutenticated['pwd'])

    if verify_pass(pwd, encodedPwd):
        worksheet.append_row([float(valor), evento, dataSerial, pagamento])
        return render_template('index.html', status='success')
    else:
        return render_template('index.html', status='error')
    
if __name__ == '__main__':
    app.run(debug=True)
