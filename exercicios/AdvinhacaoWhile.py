import random


def jogar():
    print("*******************************************")
    print("Bem vindo ao jogo de advinhação!")
    print("*******************************************")

    numero_secreto = random.randint(1, 10)
    print(numero_secreto)

    print("Qual nivel de dificuldade você deseja?")
    print("[1] -> Facil\n[2] -> Medio\n[3] -> dificil\n")
    nivel = int(input("Digite seu nivel: "))

    tentativas = 0
    descricao_nivel = " "

    while nivel < 1 or nivel > 3:
        print("Digite um numero de nivel valido!\n[1] -> Facil\n[2] -> Medio\n[3] -> dificil\n")
        nivel = int(input("Digite seu nivel: "))

    if nivel == 1:
        tentativas = 6
        descricao_nivel = "Facil"
    elif nivel == 2:
        tentativas = 5
        descricao_nivel = "Medio"
    elif nivel == 3:
        tentativas = 4
        descricao_nivel = "Dificil"

    contador = 0
    while contador < tentativas:

        print("-----> tentativa {} de {} ".format(contador + 1, tentativas))

        chute = int(input("Digite um numero de 1 a 100: "))

        if chute <= 0 or chute > 100:
            print("Perdeu uma rodada, Você deve digitar um numero de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print("-----> Voce acertou o palpite")
            break

        else:
            if maior:
                print("-----> Voce errou o palpite, seu chute foi pra cima!")

            else:
                print("-----> Você errou o palpite, seu chute foi para baixo!")

        contador += 1

    print("******************Fim do Jogo!*********************")


if __name__ == "main":
    jogar()
