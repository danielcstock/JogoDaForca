from conn import DBConnector
from roleta import Roleta

if __name__ == '__main__':
    connector = DBConnector()
    roleta = Roleta()

    connector.connect()
    connector.select("SELECT tc.nome as categoria, tp.palavra FROM tb_categoria tc INNER JOIN tb_palavra tp ON tp.categoria = tc.id")
    print(roleta.pontuacaoRodada())
