import xmlrpc.client 
from roleta import Roleta

if __name__ == '__main__':
    roleta = Roleta()
    jogador = input("Nome de jogador: ")
    proxy = xmlrpc.client .ServerProxy('http://localhost:9000')
    try:
        proxy.enter_game(jogador)
    except:
        _ = 0

    while(True):
        pontos = roleta.pontuacaoRodada()
        letra = input(f"Valendo {pontos} pontos, uma letra: ")
        try:
            resposta = proxy.send_letter(jogador, letra, pontos)
        except:
            _ = 0
        if resposta == "Fim do jogo":
            quit()
        else:
            print(resposta)
        