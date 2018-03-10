from flask import Flask, render_template, request

app = Flask(__name__)

class Jogo:
    def __init__(self,nome,categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1=Jogo("mario", "aventura", "nintendo")
jogo2=Jogo("fifa", "esporte", "play4")
lista =[jogo1,jogo2]

@app.route('/')
def ola():
    return render_template('lista.html', titulo="Meus Jogos", meusJogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():                    #pegar dados vindo do servidor
    nome=request.fomr['nome']
    categoria=request.fomr['categoria']
    console=request.fomr['console']
    jogo = Jogo(nome, categoria,console)
    lista.append(jogo)
    return render_template('lista.html', titulo="Jogo", meusJogos=lista)

app.run(debug=True)
