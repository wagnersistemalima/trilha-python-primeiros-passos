print("************************************")
print("Bem vindo ao jogo de advinhação!")
print("************************************")

numero_secreto = 42
total_de_tentativas = 3

for contador in range(0, total_de_tentativas):

    print("------> {} tentatina".format(contador + 1))

    chute = int(input("Digite um numero de 1 a 100: "))

    if (chute <= 0 or chute > 100):
        print("Perdeu uma rodada, Você deve digitar um numero de 1 a 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto


    if(acertou):
        print("Voce acertou o palpite")
        break

    elif(maior):
        print("Voce errou o palpite, seu chute foi pra cima!")

    else:
        print("Você errou o palpite, seu chute foi para baixo")

    

print("Fim do Jogo!")