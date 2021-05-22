import random

class Roleta:
    '''
        Classe da roleta de pontos do jogo da forca.
    '''

    def __init__(self):
        self.casas = range(50, 1000, 50)

    def pontuacaoRodada(self):
        x = random.randint(0, len(self.casas)-1)
        return self.casas[x]