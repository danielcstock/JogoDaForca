import flask
import random
import asyncio
from flask import request
from roleta import Roleta
from conn import DBConnector
from webclient import SocketClient

app = flask.Flask(__name__)
app.config["DEBUG"] = True
client = SocketClient()

@app.route('/points', methods=['GET'])
def getPoints():
    roleta = Roleta()
    point = {
        'value': roleta.pontuacaoRodada()
    }
    return point

@app.route('/round', methods=['GET'])
def getRound():
    conn = DBConnector()
    qry_count_categoria = conn.select("SELECT count(id) FROM tb_categoria")
    count = int(qry_count_categoria[0][0])
    qry_categoria = conn.select("SELECT id, nome FROM tb_categoria WHERE id = " + str(random.randint(1, count)))
    categoria = qry_categoria[0][0]
    qry_palavras = conn.select("SELECT id, palavra FROM tb_palavra WHERE categoria = " + str(categoria))
    
    round = {
        'category' : qry_categoria,
        'words' : qry_palavras
    }
    return round

@app.route('/place', methods=['GET'])
def getPlace():
    nome_usuario = request.args.get('nome', type = str)
    conn = DBConnector()

    contador_jogadores = asyncio.run(client.enter("ws://localhost:8765", nome_usuario))

    # conn.insert("INSERT INTO tb_usuario (id, nome) VALUES (1, 'Daniel')")
    # insert no banco do numero de jogares na partida

    return "<a href='http://localhost:5000/players'>Verificar jogadores</a>"

@app.route('/players', methods=['GET'])
def getPlayers():
    contador_jogadores = 1
    # select no banco do numero de jogadores na partida
    if contador_jogadores == 3:
        return "Todos os jogadores estao prontos!"
    else:
        return "Aguardando mais " + str(3 - contador_jogadores) + " jogador(es)...<br><a href='http://localhost:5000/players'>Verificar jogadores</a>"

app.run()