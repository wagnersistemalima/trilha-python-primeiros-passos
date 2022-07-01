import random


def jogar():
    print("************************************")
    print("Bem vindo ao jogo de advinhacao")
    print("************************************")

    numero_secreto = random.randint(1, 100)
    pontos = 1000

    print("Qual nivel de dificuldade voce deseja")
    print("[1] -> Facil\n[2] -> Medio\n[3] -> dificil\n")
    nivel = int(input("Digite seu nivel: "))

    print("Voce comecar o jogo com {} pontos".format(pontos))

    while nivel < 1 or nivel > 3:
        print("Digite um numero de nivel valido!\n[1] -> Facil\n[2] -> Medio\n[3] -> dificil\n")
        nivel = int(input("Digite seu nivel: "))

    tentativas = 0
    descricao_nivel = " "

    if nivel == 1:
        tentativas = 6
        descricao_nivel = "Facil"
    elif nivel == 2:
        tentativas = 5
        descricao_nivel = "Medio"
    elif nivel == 3:
        tentativas = 4
        descricao_nivel = "Dificil"

    for contador in range(0, tentativas):

        print("------> {} tentatina de {}, nivel {}".format(contador + 1, tentativas, descricao_nivel))

        chute = int(input("Digite um numero de 1 a 100: "))

        if chute <= 0 or chute > 100:
            print("------> Perdeu uma rodada, Voce deve digitar um numero de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print("----->Huruuuu Voce acertou o palpite")
            break

        elif maior:
            print("-----> Voce errou o palpite, seu chute foi pra cima!")
            pontos_perdidos = chute - numero_secreto
            pontos = abs(pontos - pontos_perdidos)
            print("Voce perdeu {} ponto, pontuacao atual {} pontos".format(pontos_perdidos, pontos))

        else:
            print("-----> Você errou o palpite, seu chute foi para baixo")
            pontos_perdidos = numero_secreto - chute
            pontos = abs(pontos - pontos_perdidos)
            print("Voce perdeu {} ponto, pontuacao atual {} pontos".format(pontos_perdidos, pontos))

    print("--------------- Pontos total = {}".format(pontos))
    print("******************Fim do Jogo!*********************")


if __name__ == "__main__":
    jogar()
