import random
# formatar numero para duas casas float

print("Tentativa {:.2f} e {}".format(10, 5))

print("---------------------------------")


# formatar um numero para inteiro

print("Tentativa {:7d} e {}".format(4, 5))

print("---------------------------------")

# mudar ordem para mostrar na tela sem modificar os dados

print("Ola Sr. {1} {0}".format("Coredeiro", "Leonardo"))


print("------------------------------------")

# numero randomicamente gerado de 1 a 100

numero_secreto = random.randint(1, 100)
print(numero_secreto)
print(type(numero_secreto))

result = 3 // 2

print("Result = {}".format(result))


serie = range(0, 5)

print(serie[2])



