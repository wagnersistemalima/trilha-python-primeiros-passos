import random


def jogar():
    imprime_mensagem_abertura()

    palavras = carrega_palavra_secreta()

    palavra_secreta = gerador_de_frutas(palavras).lower()

    letras_acertadas = gerador_letras_acertadas(palavra_secreta)

    print("---------- Voce tera {} chances para acertar a palavra secreta ----------".format(len(palavra_secreta)))

    print(letras_acertadas)
    print("A palavra tem {} letras".format(len(letras_acertadas)))

    status = False
    acertou = False
    pontos = 0
    errou = 0
    parada = 0

    while not status and not acertou:
        print("Jogando..........")

        chute = pede_chute()
        parada += 1
        if chute in palavra_secreta:

            if marca_chute_correto(palavra_secreta, chute, letras_acertadas):
                pontos += 10

            if "_" in letras_acertadas:
                mensagem_quandro_pontuacao(letras_acertadas, pontos, errou)

            else:
                mensagem_ganhou_fim_game(pontos, palavra_secreta)

                status = True
                acertou = True
        elif chute not in palavra_secreta:
            errou += 3
            mensagem_errou_chute(errou)

        if parada == len(palavra_secreta) + 5:
            mensagem_encerrando_tentativas(palavra_secreta)
            status = True
            acertou = True

    mensagem_encerramento_jogo(pontos, errou)


def imprime_mensagem_abertura():
    print("*******************************************")
    print("Bem vindo ao jogo Forca!")
    print("*******************************************")
    print("-----> Acerte a palavra secreta <----------")
    print("-----> Dica: É uma fruta <-----------------")


def carrega_palavra_secreta() -> list:
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    return palavras


def gerador_de_frutas(lista: list) -> str:
    escolha_palavra_secreta = random.randint(0, len(lista))

    palavra_secreta = lista[escolha_palavra_secreta]

    return palavra_secreta


def gerador_letras_acertadas(palavra: str):
    lista_letras_acertadas = ["_" for letra in palavra]
    return lista_letras_acertadas


def pede_chute() -> str:
    chute = input("Qual letra? ").strip().lower()
    return chute


def marca_chute_correto(palavra_secreta: str, chute: str, letras_acertadas: list) -> bool:
    index = 0
    status = False
    for letra in palavra_secreta:

        if chute == letra and chute not in letras_acertadas[index]:
            letras_acertadas[index] = letra
            status = True

        index += 1
    return status


def mensagem_encerrando_tentativas(palavra_secreta: str):

    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mensagem_errou_chute(errou: int):
    print("Voce errou, tente novamente")
    print("Pontos perdidos {}".format(errou))


def mensagem_quandro_pontuacao(letras_acertadas: list, pontos: int, errou: int):
    print("Ainda falta acertar {} letras".format(letras_acertadas))
    print("Pontuacao acertos = {}".format(pontos))
    print("Pontuacao erros = {}".format(errou))


def mensagem_encerramento_jogo(pontos, errou):
    print("******************Pontuacao acertos = {} *********************".format(pontos))
    print("******************Pontuacao erros = {} *********************".format(errou))
    print("******************Pontuacao Final = {} *********************".format(pontos - errou))
    print("******************Fim do Jogo!*********************")


def mensagem_ganhou_fim_game(pontos: int, palavra_secreta: str):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Pontuacao = {}".format(pontos))
    print("Palavra secreta = {}".format(palavra_secreta))




if __name__ == "__main__":
    jogar()
