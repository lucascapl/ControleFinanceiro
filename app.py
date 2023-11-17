from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    valor = request.form.get('valor')
    evento = request.form.get('evento')
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

    # Append de uma nova linha
    worksheet.append_row([float(valor), evento, dataString, pagamento])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
