from flask import Flask

# Criar uma instância do aplicativo Flask
app = Flask(__name__)

# Definir uma rota para a página inicial
@app.route('/')
def index():
    return 'Bem-vindo ao meu site Flask!'

# Executar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
