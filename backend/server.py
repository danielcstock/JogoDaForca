import asyncio
from websockets import serve

class Server:
    def __init__(self):
        self.word = self.getWord()
        self.hidden = "_" * len(self.word)
        self.players = {}

    def getWord(self):
        return "abelha"

    def printWord(self, command):
        command = command.split(":") 
        player = command[0]
        letter = command[1]
        points = command[2]
        if len(letter) == 1:
            print(f"{player} - {letter} - {points}")
            for i, l in enumerate(self.word):
                if letter == l and self.hidden[i] == "_":
                    self.hidden = self.hidden[:i] + letter + self.hidden[i+1:]
                    self.players[player] += int(points)
        print(self.hidden)

    def checkWord(self):
        if "_" in self.hidden:
            return False
        return True

    def registerPlayer(self, message):
        player = message.split(":")[0]
        if player not in self.players:
            self.players[player] = 0
        if len(self.players) >= 3:
            keys = self.players.keys()
            return True
        return False

    def getWinner(self):
        print(f"Placar final:\n{self.players}")
                

    async def round(self, websocket, path):
        async for message in websocket:
            await websocket.send(message)
            if self.registerPlayer(message):
                self.printWord(message)
                if self.checkWord():
                    print("Fim do jogo")
                    self.getWinner()
                    quit()
            else:
                print("Aguardando outros jogadores.")
    
    async def main(self, port):
        async with serve(self.round, "localhost", port):
            await asyncio.Future()
    
    def start(self, port):
        asyncio.run(self.main(port))