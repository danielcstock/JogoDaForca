import asyncio
from websockets import connect

class SocketClient:
    def __init__(self):
        self.contador_jogadores = 0

    async def enter(self, uri, message):
        self.contador_jogadores += 1
        async with connect(uri) as websocket:
            await websocket.send(message)
            await websocket.recv()
        return self.contador_jogadores


#    asyncio.run(hello("ws://localhost:8765", "A"))
        