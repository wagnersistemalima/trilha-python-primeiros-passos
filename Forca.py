def jogar():
    print("*******************************************")
    print("Bem vindo ao jogo Forca!")
    print("*******************************************")
    print("-----> Acerte a palavra secreta <----------")
    print("-----> Dica: É uma fruta <-----------------")

    palavra_secreta = "banana"
    status = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print("A palavra tem {} letras".format(len(letras_acertadas)))
    print(letras_acertadas)

    while not status and not acertou:
        print("Jogando..........")

        chute = input("Qual letra? ").strip()

        index = 0
        for letra in palavra_secreta:

            if chute.lower() == letra.lower():
                letras_acertadas[index] = letra

            index += 1
        if "_" in letras_acertadas:
            print("Ainda falta acertar {} letras".format(letras_acertadas))
        else:
            print("Parabéns você acertou!")
            status = True
            acertou = True

    print("******************Fim do Jogo!*********************")


if __name__ == "__main__":
    jogar()
