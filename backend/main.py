import asyncio
from server import Server
from webclient import SocketClient
from roleta import Roleta

def getHint():
    return "Animal"

def startRound():
    print("Rodada 1:\n")
    print("Dica: " + getHint())

if __name__ == '__main__':
    portas = [8765, 8766, 8767]
    server = Server()
    
    for porta in portas:
        try:
            server.start(porta)
        except:
            print("Tentando reconectar...\n")
    quit()

    
    

