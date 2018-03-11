from flask import Flask, render_template, request, redirect,session,flash

app = Flask(__name__)
app.secret_key="chave"

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
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    jogo = Jogo(nome, categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash(request.form['usuario'] + 'logou com sucesso')
        return redirect('/')
    else:
        flash('Tente novamente')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Nenhum usuário logado")
    return redirect('/')
app.run(debug=True)
