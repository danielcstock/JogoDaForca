import asyncio
from websockets import serve

word = "abelha"
hidden = "_" * len(word)

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
        printWord(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

def printWord(letter):
    for i, l in enumerate(word):
        if letter == l and hidden[i] == "_":
            hidden = hidden[:i] + letter + hidden[i+1:]
    print(hidden)

asyncio.run(main())