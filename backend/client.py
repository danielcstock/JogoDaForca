import asyncio
from webclient import SocketClient
from roleta import Roleta

def getHint():
    return "Animal"

def startRound():
    print("Rodada 1:\n")
    print("Dica: " + getHint())

def getPoints():
    return 200

if __name__ == '__main__':
    portas = [8765, 8766, 8767]
    clients = list()
    roleta = Roleta()
    uri = "ws://localhost"

    jogador = input("Nome de jogador: ")
    for porta in portas:
        clients.append(SocketClient(f"{uri}:{porta}", jogador))

    startRound()

    for client in clients:
            try:
                client.setPoints(0)
                asyncio.run(client.sendLetter("inicio"))
            except:
                print("")

    while(True):
        points = roleta.pontuacaoRodada()
        letra = input("Valendo " + str(points) +" pontos, uma letra: ")
        for client in clients:
            try:
                client.setPoints(points)
                asyncio.run(client.sendLetter(letra))
            except:
                print("")