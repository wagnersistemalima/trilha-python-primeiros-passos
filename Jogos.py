import Forca
import AdvinhacaoFor


def escolha_jogar():
    print("*******************************************")
    print("Escolha o seu jogo")
    print("*******************************************")

    print("[1] Opcao do Jogo Advinhacao\n[2] Opcao Jogo forca")

    opcao = int(input("Sua opcao sera: "))

    if opcao == 1:
        print("---> Jogando Advinhacao!")
        AdvinhacaoFor.jogar()

    elif opcao == 2:
        print("---> Jogando Forca!")
        Forca.jogar()


if __name__ == "__main__":
    escolha_jogar()
