from flask import Flask, render_template

app = Flask(__name__)
@app.route('/inicio')
def ola():
    lista =["jogo1", "jogo2", "jogo3"]
    return render_template('lista.html', titulo="Meus Jogos", meusJogos=lista)


app.run()
