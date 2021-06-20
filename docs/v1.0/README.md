## Instalação dos pacotes do projeto :inbox_tray:

### Ambiente Python :keyboard:
```
sudo apt-get install python
```
```
sudo apt-get install pip
```
(websockets)[https://github.com/aaugustin/websockets]
```
pip install websockets
```
(asyncio)[]
```
pip install asyncio
```

## Iniciar aplicação
Para rodar a aplicação é necessário abrir um terminal-server e outro terminal-client.

### Server
O terminal-server exibe a palavra da rodada e as tentativas de cada jogador.

```
python3 backend/main.py
```

### Client
O terminal-client exibe a pontuação que o jogador poderá ganhar a cada rodada, se acertar, e recebe o input do jogador.

```
python3 backend/client.py
```

![image](https://user-images.githubusercontent.com/30013171/122686384-0f57e080-d1e7-11eb-8dbd-dc96bf7333de.png)
