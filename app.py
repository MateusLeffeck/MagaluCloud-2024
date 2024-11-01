from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    instancia = request.form['instancia']
    armazenamento = request.form['armazenamento']
    ssh = request.form['ssh']
    tempo = request.form['tempo']
    familia_tipo = request.form['radio']
    ip_publico = 1 if 'option1' in request.form else 0

    csv_file = 'dados.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Nome', 'Email', 'Instância', 'Armazenamento', 'SSH', 'Tempo', 'Família Tipo', 'IP Público'])
        writer.writerow([nome, email, instancia, armazenamento, ssh, tempo, familia_tipo, ip_publico])

    return "Dados enviados e salvos com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
