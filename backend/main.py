import requests
import asyncio
from webclient import SocketClient

if __name__ == '__main__':
    response = requests.get("http://localhost:5000/getPoints")
    if response.status_code == 200:
        print(response.json()["value"])
    client = SocketClient()

    while(True):
        letra = input()
        asyncio.run(client.hello("ws://localhost:8765", letra))
