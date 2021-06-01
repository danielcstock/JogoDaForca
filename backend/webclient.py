import asyncio
from websockets import connect

class SocketClient:
    async def hello(self, uri, message):
        async with connect(uri) as websocket:
            await websocket.send(message)
            await websocket.recv()

#    asyncio.run(hello("ws://localhost:8765", "A"))
        