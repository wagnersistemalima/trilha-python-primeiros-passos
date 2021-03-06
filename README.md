# trilha-python-primeiros-passos
Trabalhando com a nova versao da linguagem python, criando um joguinho de advinhação e forca


## Jogo de advinhação

* Um simples jogo feito em Python chamado: Adivinha. Nele você terá que acerta o número que foi
gerado aleatoriamente entre 1 e 100, ao decorrer do jogo você recebe dicas e possui niveis de dificuldade para acertar

![alter text](https://github.com/wagnersistemalima/trilha-python-primeiros-passos/blob/main/images/image-advinhacao1.png)



## Jogo forca

* O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras e o tema ligado à palavra.

![alter text](https://github.com/wagnersistemalima/trilha-python-primeiros-passos/blob/main/images/image-forca1.png)

![alter txt](https://github.com/wagnersistemalima/trilha-python-primeiros-passos/blob/main/images/image-forca2.png)


## Para criar esses joguinhos utilizamos algumas estruturas de dados em python

* List , estrutura de dados que nos permite guardar valores. Essa estrutura é a lista. Para criar uma lista, utilizamos colchetes ex:

```

valores = []
type(valores)
class 'list'

```

* No jogo da forca, criei um uma função para gerar frutas e armazenar em uma lista, escolhendo aleatoriamente uma fruta para iniciar o jogo

```
def gerador_de_frutas():
    lista_de_palavras_secretas = ["banana", "jaboticaba", "melancia", "graviola", "laranja", "maracujar"]
    escolha_palavra_secreta = random.randint(0, len(lista_de_palavras_secretas))

    palavra_secreta = lista_de_palavras_secretas[escolha_palavra_secreta]

    return palavra_secreta

```

* O interpretador do Python possui várias funções e tipos embutidos que sempre estão disponíveis, Built-in

```

len()              Devolve o comprimento (o número de itens) de um objeto.
print()            Mostrar na tela
inpult()           A função então lê uma linha da fonte de entrada, converte a mesma para uma string
max()              Devolve o maior item em um iterável ou o maior de dois ou mais argumentos.

```

* Tupla , mais um tipo de sequencia em python que é uma lista imutavel

```
filmes = ("The Lord of the Rings", "O homem de ferro", "Os Vingadores")
type(filmes)
class 'tuple'
```

* Para transformar um tuple em uma lista, temos a função

```
tupla1 = (1, "Wagner")

lista = list(tupla1)                  De tupla para list

transformado = tuple(lista)                De list para tuple
```

## Conhecendo o set

* Coleção onde não podem existir elementos duplicados

```
lista_sem_repeticao = {"wagner", "marina", "karina"}
type(lista_sem_repeticao)
class 'set'
```
* Adicionando elementos no set

```
lista_sem_repeticao.add("marco")
```

* set não possui um índice
* É importante notar que o set não é uma sequência, pois não tem um índice
* Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.


## Conhecendo o dictionary


```
dicionario = {1: "wagner", 2: "marina", 3: "karina"}
type(dicionario)
class 'dict'
```

* Nesse par, temos no lado esquerdo a chave e no lado direito o valor. Isso é importante pois usamos a chave para recuperar um valor

```
usuario = dicionario[2]

print(usuario)

-> mostra na tela = marina
```
* List Comprehension. para criar uma lista com os mesmos dados de frutas com letras maiusculas

```
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]

```

* O recurso List Comprehension também permite utilizar condições para o preenchimento da lista.

```
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_de_numeros_pares = [numero for numero in lista if numero % 2 == 0]

print(lista_de_numeros_pares)

[2, 4, 6, 8]

```

## Ler um arquivo em python

```
# para utilizar a função open para leitura

arquivo = open("palavras.txt", "r")

arquivo.close()

# para utilizar a função open para escrita dando apend no arquivo

arquivo2 = open("palavra2.txt", "a")

arquivo2.close()

# para utilizar a função open para escrita, porem vai apagar os dados existentes

arquivo3 = open("palavra3.txt", "w")

arquivo3.close()
```

* ler apenas a primeira linha do arquivo

```
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)

arquivo.close()
```
