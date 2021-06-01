## Instalação dos pacotes do projeto :inbox_tray:

### Docker :whale:
Todo o projeto é rodado em container Docker, logo, é preciso instalar alguns pacotes antes de executar o jogo.
Siga o tutorial abaixo para instalar corretamente as ferramentas necessárias no ambiente linux (Ubuntu).

- Desinstale versões antigas do Docker:
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

- Instale as dependências e prepare o repositório para download

```
sudo apt-get update
```
```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```    
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```
sudo apt-get update
```
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

- Escolha a versão para instalação
```
apt-cache madison docker-ce
```
```
sudo apt-get install docker-ce=5:20.10.6~3-0~ubuntu-groovy docker-ce-cli=5:20.10.6~3-0~ubuntu-groovy containerd.io
```

### MariaDB :notebook_with_decorative_cover:

```
docker run -p 127.0.0.1:3306:3306  --name mariadb-JogoDaForca -e MARIADB_ROOT_PASSWORD=jdf-abc -d mariadb
```

### Ambiente Python :keyboard:
```
sudo apt-get install python
```
```
sudo apt-get install pip
```
```
sudo apt install libmariadb3 libmariadb-dev
```
```
pip install flask
```
```
pip install mariadb
```
```
pip install requests
```
(websockets)[https://github.com/aaugustin/websockets]
```
pip install websockets
```
(asyncio)[]
```
pip install asyncio
```