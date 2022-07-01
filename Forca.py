def jogar():
    print("*******************************************")
    print("Bem vindo ao jogo Forca!")
    print("*******************************************")

    palavra_secreta = "banana"
    status = False
    acertou = False

    while not status and not acertou:
        print("Jogando..........")

        chute = input("Qual letra? ").strip()

        index = 0
        for letra in palavra_secreta:

            if chute.lower() == letra.lower():
                print("Encontrei a letra {} na posição {}".format(chute, index))

            else:
                print("Opss não encontrei a letra {}".format(chute))

            index += 1

    print("******************Fim do Jogo!*********************")


if __name__ == "__main__":
    jogar()
