import requests

if __name__ == '__main__':
    # connector.select("SELECT tc.nome as categoria, tp.palavra FROM tb_categoria tc INNER JOIN tb_palavra tp ON tp.categoria = tc.id")
    response = requests.get("http://localhost:5000/getPoints")
    if response.status_code == 200:
        print(response.json()["value"])
