

print("************************************")
print("Bem vindo ao jogo de advinhação!")
print("************************************")

numero_secreto = 42
total_deTentativas = 3


contador = 0
while (contador < total_deTentativas):

    print("-----> tentativa {} ".format(contador + 1))

    chute = int(input("Digite um numero de 1 a 100: "))
    print("numero digitado é ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if(acertou):
        print("Voce acertou o palpite")
        break

    else:
        if(maior):
            print("Voce errou o palpite, seu chute foi pra cima!")

        else:
            print("Você errou o palpite, seu chute foi para baixo")

    contador += 1


print("Fim do Jogo!")