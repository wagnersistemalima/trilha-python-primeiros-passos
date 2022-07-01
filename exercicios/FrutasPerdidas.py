# Exercicios de lista, frutas perdidas

print("----------------------  Frutas perdidas----------------------------")


frutas = ["banana", "maça", "pera", "uva"]

frutas_perdidas = input("Qual a fruta perdida? ")


if frutas_perdidas in frutas:
    print("Sim, temos essa fruta")
else:
    print("Não temos essa fruta")


print("----------------------  Fim ---------------------------")