import flask
import random
import asyncio
import requests
from flask import request
from roleta import Roleta
from conn import DBConnector
from webclient import SocketClient
from jogo import Jogo

app = flask.Flask(__name__)
app.config["DEBUG"] = True
client = SocketClient()
conn = DBConnector()
jogo = Jogo()

@app.route('/points', methods=['GET'])
def getPoints():
    roleta = Roleta()
    point = {
        'value': roleta.pontuacaoRodada()
    }
    return point["value"]

@app.route('/place', methods=['GET'])
def getPlace():
    nome_usuario = request.args.get('nome', type = str)
    
    asyncio.run(client.enter("ws://localhost:8765", nome_usuario))
    jogador_id =  conn.executeQuery("SELECT id FROM tb_usuario WHERE nome LIKE '" + nome_usuario + "' LIMIT 1")
    if not jogador_id:
        conn.insert("INSERT INTO tb_usuario (nome) VALUES ('"+ nome_usuario +"')")
        jogador_id =  conn.executeQuery("SELECT id FROM tb_usuario WHERE nome LIKE '" + nome_usuario + "' LIMIT 1")
    qry_partida = conn.executeQuery("SELECT * FROM tb_partida ORDER BY id DESC LIMIT 1")
    jogador_id = jogador_id[0][0]

    if not qry_partida:
        conn.insert("INSERT INTO tb_partida (jogador_1) VALUES (" + str(jogador_id) + ")")
        qry_partida = conn.executeQuery("SELECT * FROM tb_partida ORDER BY id DESC LIMIT 1")
        jogo.criarPartida(qry_partida[0][0])
    else:
        jogador_1 = qry_partida[0][1]
        jogador_2 = qry_partida[0][2]
        jogador_3 = qry_partida[0][3]
        if not jogador_1:
            conn.update("tb_partida", "jogador_1", jogador_id, qry_partida[0][0])
        elif not jogador_2:
            conn.update("tb_partida", "jogador_2", jogador_id, qry_partida[0][0])
        elif not jogador_3:
            conn.update("tb_partida", "jogador_3", jogador_id, qry_partida[0][0])

    return "<a href='players?partida=" + str(qry_partida[0][0]) +"'>Verificar jogadores</a>"

@app.route('/players', methods=['GET'])
def getPlayers():
    partida = request.args.get('partida', type = str)

    qry_partida = conn.executeQuery("SELECT * FROM tb_partida WHERE id = " + str(partida))
    if not qry_partida[0][2]:
        return "Aguardando mais 2 jogador(es)...<br><a href='players?partida=" + str(partida) + "'>Verificar jogadores</a>"
    elif not qry_partida[0][3]:
        return "Aguardando mais 1 jogador(es)...<br><a href='players?partida=" + str(partida) + "'>Verificar jogadores</a>"
    return "Todos os jogadores estao prontos!<br><a href='match?partida=" + partida + "'>Comecar</a>"

@app.route('/match', methods=['GET'])
def play():
    partida = request.args.get('partida', type = str)
    players = jogo.buscarJogadores(partida)
    words = jogo.buscarPalavras(partida)
    hint = jogo.buscarDica(partida)

    palavra_1 = words[0][0]
    palavra_2 = words[1][0]
    palavra_3 = words[2][0]

    jogador_1 = players[0][1]
    jogador_2 = players[1][1]
    jogador_3 = players[2][1]
    
    return "<h1>Roda a Roda</h1>\
        <div id='quadro'>\
        <span id='palavra-1'>" + "_ " * len(palavra_1) + "</span><br>\
        <span id='palavra-2'>" + "_ " * len(palavra_2) + "</span><br>\
        <span id='palavra-3'>" + "_ " * len(palavra_3) + "</span><br><br>\
        <span id='dica'>Dica: " + str(hint) +"</span><br><br>\
        </div>\
        <div id='jogador-1'>\
        <span>" + jogador_1 + ":</span>\
        <span>0</span>\
        </div>\
        <div id='jogador-2'>\
        <span>" + jogador_2 + ":</span>\
        <span>0</span>\
        </div>\
        <div id='jogador-3'>\
        <span>" + jogador_3 + ":</span>\
        <span>0</span>\
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