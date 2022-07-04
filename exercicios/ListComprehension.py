# criar lista de numeros pares usando list comprehension

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_de_numeros_pares = [numero for numero in lista if numero % 2 == 0]

print(lista_de_numeros_pares)