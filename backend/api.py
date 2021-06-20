import flask
import random
import asyncio
import requests
from flask import request
from roleta import Roleta
from conn import DBConnector
from webclient import SocketClient

app = flask.Flask(__name__)
app.config["DEBUG"] = True
client = SocketClient()
conn = DBConnector()

@app.route('/points', methods=['GET'])
def getPoints():
    roleta = Roleta()
    point = {
        'value': roleta.pontuacaoRodada()
    }
    return point

@app.route('/round', methods=['GET'])
def getRound():
    qry_count_categoria = conn.count("tb_categoria", "id")
    count = int(qry_count_categoria[0][0])
    qry_categoria = conn.executeQuery("SELECT id, nome FROM tb_categoria WHERE id = " + str(random.randint(1, count)))
    categoria = qry_categoria[0][0]
    qry_palavras = conn.executeQuery("SELECT id, palavra FROM tb_palavra WHERE categoria = " + str(categoria))
    
    round = {
        'category' : qry_categoria,
        'words' : qry_palavras
    }
    return round

@app.route('/place', methods=['GET'])
def getPlace():
    nome_usuario = request.args.get('nome', type = str)
    
    contador_jogadores = asyncio.run(client.enter("ws://localhost:8765", nome_usuario))

    conn.insert("INSERT INTO tb_usuario (nome) VALUES ('"+ nome_usuario +"')")
    jogador_id =  conn.executeQuery("SELECT id FROM tb_usuario WHERE nome LIKE '" + nome_usuario + "' LIMIT 1")
    qry_partida = conn.executeQuery("SELECT * FROM tb_partida ORDER BY id DESC LIMIT 1")
    
    if not qry_partida or qry_partida[0][3]:
        conn.executeQuery("INSERT INTO tb_partida (jogador_1) VALUES (" + str(jogador_id[0][0]) + ")")
    else:
        jogador_1 = qry_partida[0][1]
        jogador_2 = qry_partida[0][2]
        jogador_3 = qry_partida[0][3]
        if not jogador_1:
            conn.update("tb_partida", "jogador_1", jogador_id[0][0], qry_partida[0][0])
        elif not jogador_2:
            conn.update("tb_partida", "jogador_2", jogador_id[0][0], qry_partida[0][0])
        elif not jogador_3:
            conn.update("tb_partida", "jogador_3", jogador_id[0][0], qry_partida[0][0])
    print(qry_partida)

    return "<a href='players?partida=" + str(qry_partida[0][0]) +"'>Verificar jogadores</a>"

@app.route('/players', methods=['GET'])
def getPlayers():
    partida = request.args.get('partida', type = str)

    qry_partida = conn.executeQuery("SELECT * FROM tb_partida WHERE id = " + str(partida))
    if not qry_partida[0][2]:
        return "Aguardando mais 2 jogador(es)...<br><a href='players?partida=" + str(partida) + "'>Verificar jogadores</a>"
    elif not qry_partida[0][3]:
        return "Aguardando mais 1 jogador(es)...<br><a href='players?partida=" + str(partida) + "'>Verificar jogadores</a>"
    return "Todos os jogadores estao prontos!<br><a href='match'>Comecar</a>"

@app.route('/match', methods=['GET'])
def play():
    round = requests.get("http://localhost:5000/round")
    payload = round.json()
    palavra_1 = payload["words"][0][1]
    palavra_2 = payload["words"][1][1]
    palavra_3 = payload["words"][2][1]
    return "<h1>Roda a Roda</h1>\
        <div id='quadro'>\
        <span id='palavra-1'>" + palavra_1 + "</span><br>\
        <span id='palavra-2'>" + palavra_2 + "</span><br>\
        <span id='palavra-3'>" + palavra_3 + "</span><br><br>\
        <span id='dica'>Dica: " + str(payload["category"][0][1]) +"</span><br><br>\
        </div>\
        <div id='jogador-1'>\
        <span>Nome</span>\
        <span>Pontos</span>\
        </div>\
        <div id='jogador-2'>\
        <span>Nome</span>\
        <span>Pontos</span>\
        </div>\
        <div id='jogador-3'>\
        <span>Nome</span>\
        <span>Pontos</span>\
        </div>\
        <div>\
        <form action='http://localhost:5000/place'>\
        <input type='submit' value='Girar a roda'>\
        </form>\
        <form>\
        <label for='letra'>Letra:</label>\
        <input type='text' id='letra' name='letra'><br><br>\
        <input type='submit' value='Enviar'>\
        </form>\
        </div>"

app.run()