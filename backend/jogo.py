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

    def buscarJogadores(self, partida):
        jogadores = self.conn.executeQuery(\
                "SELECT tu.id, tu.nome FROM tb_usuario tu \
                WHERE tu.id IN (SELECT jogador_1 FROM tb_partida WHERE id = " + partida + ") OR \
                tu.id IN (SELECT jogador_2 FROM tb_partida WHERE id = " + partida + ") OR \
                tu.id IN (SELECT jogador_3 FROM tb_partida WHERE id = " + partida + ")")
        return jogadores

    def buscarPalavras(self, partida):
        palavras = self.conn.executeQuery(\
                "SELECT p.palavra FROM tb_palavra p \
                WHERE id IN (SELECT palavra_1 FROM tb_partida WHERE id = " + partida + ") OR \
                id IN (SELECT palavra_2 FROM tb_partida WHERE id = " + partida + ") OR \
                id IN (SELECT palavra_3 FROM tb_partida WHERE id = " + partida + ")")
        return palavras

    def buscarDica(self, partida):
        dica = self.conn.executeQuery("SELECT c.nome FROM tb_categoria c \
                WHERE id IN (SELECT dica FROM tb_partida WHERE id = " + partida + ")")
        return dica[0][0]