from websockets import connect

class SocketClient:
    def __init__(self, uri, player):
        self.name = player
        self.points = 0
        self.uri = uri
    
    def setPoints(self, points):
        self.points = points

    async def sendLetter(self, message):
        async with connect(self.uri) as websocket:
            await websocket.send(f"{self.name}:{message}:{self.points}")
            await websocket.recv()
        