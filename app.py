from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav'}

# Cria o diretório de uploads se não existir
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Inicializa o banco de dados em memória
db = {
    'A1': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'B1': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'C1': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'D1': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'E1': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'A2': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'B2': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'C2': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'D2': {'Sala': 'Sala', 'Audio': 'No Audio'},
    'E2': {'Sala': 'Sala', 'Audio': 'No Audio'},
}

# Função para verificar se o arquivo é permitido
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Rota principal que renderiza a página inicial
@app.route('/')
def index():
    return render_template_string('''
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <style>
        /* Estilos CSS para a página */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            width: 100%;
            max-width: 500px;
            margin: auto;
            padding: 20px;
            box-shadow: 0px 0px 10px 0px #0000001a;
            background-color: #fff;
        }
        .logo {
            width: 5cm;
            align-self: center;
            margin: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        td {
            border: 1px solid #e3e3e3;
            padding: 1em;
            background-color: #f4f4f4;
        }
        td.key {
            width: 3cm;
            text-align: center;
        }
        td.sala {
            width: 12cm;
            text-align: center;
        }
        td.audio {
            width: 10cm;
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #e3e3e3;
            margin-left: 20px;
            margin-right: 20px;
        }
        label, input, button {
            margin: 5px;
        }
        input[name="key"] {
            width: 3cm;
        }
        input[name="sala"], input[type="file"] {
            width: 10cm;
        }
        button {
            width: 4.5cm;
            cursor: pointer;
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
    <div class="container">
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo" class="logo">
        <table>
            <thead>
                <tr>
                    <th class="key">ID</th>
                    <th class="sala">Sala</th>
                    <th class="audio">Áudio</th>
                </tr>
            </thead>
            <tbody>
                {% for key, value in db.items() %}
                    <tr>
                        <td class="key">{{ key }}</td>
                        <td class="sala">{{ value['Sala'] }}</td>
                        <td class="audio">{{ value['Audio'] }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <form method="post" action="/update">
            <label for="key">ID:</label>
            <input type="text" name="key" required>
            <label for="sala">Sala:</label>
            <input type="text" name="sala" required>
            <button type="submit">Atualizar</button>
        </form>
        <form method="post" action="/delete">
            <label for="key">ID:</label>
            <input type="text" name="key" required>
            <button type="submit">Apagar</button>
        </form>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <label for="key">ID:</label>
            <input type="text" name="key" required>
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
    </div>
    ''', db=db)

@app.route('/upload', methods=['POST'])
def upload_file():
    key = request.form.get('key')
    if 'file' not in request.files or key not in db:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        db[key]['Audio'] = filename
        return redirect(url_for('index'))
    else:
        return "File type not allowed!", 400

@app.route('/update', methods=['POST'])
def update():
    key = request.form.get('key')
    sala = request.form.get('sala')
    if key in db:
        db[key]['Sala'] = sala
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    key = request.form.get('key')
    if key in db:
        db[key]['Sala'] = 'Sala'
        audio_file = db[key]['Audio']
        if audio_file != 'No Audio':  # Verifica se há um arquivo de áudio para remover
            os.remove(audio_file)  # Remove o arquivo de áudio sem adicionar o prefixo 'uploads\\' novamente
            db[key]['Audio'] = 'No Audio'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

