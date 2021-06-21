from xmlrpc.server import SimpleXMLRPCServer
import logging
import os
import random

# Game variables
players = {}
round = {}

# Set up logging
server = SimpleXMLRPCServer(('localhost', 9000), logRequests=False)

# Expose a function
def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    return os.listdir(dir_name)
server.register_function(list_contents)

def enter_game(player):
    if len(players) < 3:
        print(f"{player} entrou no jogo.")
        players[player] = 0
    else:
        print("A sala está cheia.")
    if len(players) == 3:
        palavra = getRandomLine()
        word = start_game(getWord(palavra), getHint(palavra))
server.register_function(enter_game)

def send_letter(player, letter, points):
    return printWord(player, letter, points)
server.register_function(send_letter)

def start_game(word, hint):
    hidden = "_" * len(word)
    print(f"\nDica: {hint}\n{hidden}")
    round["hidden"] = hidden
    round["word"] = word

def getRandomLine():
    arquivo = open('palavras.txt', 'r')
    lista_palavras = arquivo.readlines()
    linha = random.choice(lista_palavras)
    return linha

def getWord(palavra):
    palavra = palavra.split(":")[0]
    return palavra

def getHint(palavra):
    dica = palavra.split(":")[1]
    return dica

def printWord(player, letter, points):
    retorno = "Errou"
    hidden = round["hidden"]
    word = round["word"]
    if len(letter) == 1:
        print(f"{player} - {letter} - {points}")
        for i, l in enumerate(word):
            if letter == l and hidden[i] == "_":
                hidden = hidden[:i] + letter + hidden[i+1:]
                players[player] += int(points)
                round["hidden"] = hidden
                retorno = "Acertou"
    print(hidden)
    if checkWord(hidden):
        print(f"Placar final:\n{players}")
        server.server_close()
        retorno = "Fim do jogo"
    return retorno

def checkWord(hidden):
    if "_" in hidden:
        return False
    return True

try:
    print("Aguardando jogadores")
    server.serve_forever()
except KeyboardInterrupt:
    print("Exiting")