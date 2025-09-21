#!/usr/bin/env python 3

#FOR = Opera em cima de uma coleção

#lista materializada
numbers = [1,2,3,4,5,6,]
#imprima a partir do 2º elemento
print(numbers[2:])

#Objeto iterador que cria uma lista não materializada, usando start, next, stop. Logo, ocupa menos memória.
numbers1 = range(1,6) #vai criar uma lista de 1 a 5
for number in numbers1:
    print(number)

#usando step para dar um pulo no range = vai criar uma lista de 1 a 5 exibindo, pulando 2 números
numbers2 = range(1,6,2)
for number in numbers2:
    print(number)

#criar uma lista não materializada de 1 a 11 e exibir apenas os pares, com uso de CONTINUE
numbers3 = range(1,11)
for number in numbers3:
    par = number %2 == 0
    if par:
        print(number)
    else:
        continue #volta para o início do for sem fazer o resto do código (se for ímpar não vai imprimir o print abaixo)
    print(f"essa parte só imprime se o {number} for par.")

#criar uma lista não materializada de 1 a 11 e exibir apenas os pares, com uso de BREAK
numbers4 = range(1,11)
for number in numbers4:
    par = number %2 == 0
    if par:
        print(number)
    else:
        break #no 1º loop verificou que 1 não é par e para a execução do código (não vai printar nada)
    print(f"essa parte só imprime se o {number} for par.")

#criando uma lista "nova" a partir de "existente" multiplicada por 3
existente = [1,2,3]
#nova lista começa vazia
nova = []
for n in existente:
    nova.append(n * 3)
print(nova)

#FUNCIONAL = criando uma lista "nova" a partir de "existente" multiplicada por 3
#LIST COMPREHENSION = para criar uma nova lista
existente1 = [1,2,3]
nova1 = [n * 3 for n in existente1]
print(nova1)