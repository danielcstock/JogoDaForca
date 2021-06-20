from roleta import Roleta
from conn import DBConnector
import random

class Jogo:
    def __init__(self):
        self.conn = DBConnector()

    def criarPartida(self, id):
        qry_count_categoria = self.conn.count("tb_categoria", "id")
        count = int(qry_count_categoria[0][0])
        qry_categoria = self.conn.executeQuery("SELECT id, nome FROM tb_categoria WHERE id = " + str(random.randint(1, count)))
        categoria = qry_categoria[0][0]
        qry_palavras = self.conn.executeQuery("SELECT id, palavra FROM tb_palavra WHERE categoria = " + str(categoria))

        self.conn.update("tb_partida", "palavra_1", qry_palavras[0][0], id)
        self.conn.update("tb_partida", "palavra_2", qry_palavras[1][0], id)
        self.conn.update("tb_partida", "palavra_3", qry_palavras[2][0], id)
        self.conn.update("tb_partida", "dica", categoria, id)