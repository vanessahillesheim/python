#!/usr/bin/env python3

#criando conjuntos
#usar a classe set() 
#set são objetos de transição = não guardam valores
#set cria uma série de elementos não ordenados, sem repetição, que não permite duplicidade


conjunto_a = [1,2,3,4,5]
conjunto_b = [4,5,6,7,8]

#UNIÃO DE CONJUNTOS (operador | ou .union)
uniao = set(conjunto_a) | set(conjunto_b)
print(uniao)

union = set(conjunto_a).union(set(conjunto_b))
print(union)

#o ideal é já criar o  objeto com set

conjunto_c = set([1,2,3,4,5])
conjunto_d = set([4,5,6,7,8])

uniao1 = conjunto_c | conjunto_d
print(uniao1)

union1 = conjunto_c.union(conjunto_d)
print(union1)

#INTERSECÇÃO DE CONJUNTOS (operador & ou .intersection)
interseccao = set(conjunto_a) & set(conjunto_b)
print(interseccao)

interseccao1 = conjunto_c.intersection(conjunto_d)
print(interseccao1)

#DIFERENÇA ENTRE CONJUNTOS (operador - ou .difference)
difference = set(conjunto_a) - set(conjunto_b)
print(difference)

diferenca = set(conjunto_b) - set(conjunto_a)
print(diferenca)

difference1 = conjunto_c - conjunto_d
print(difference1)

diferenca1 = conjunto_d.difference(conjunto_c)
print(diferenca1)

#DIFERENÇA SIMÉTRICA = para pegar todos os itens diferentes entre grupos (operador ^ou symmetric_difference)

symmetric = set(conjunto_a) ^ set(conjunto_b)
print(symmetric)

simetrico = conjunto_c.symmetric_difference(conjunto_d)
print(simetrico)

#HASH Table
#serve para fazer pesquisa; usando o hash, diminui o tempo/tamanho da pesquisa
numeros = [1,2,3,4,1,1,1,1,7,8,9]

#para verificar se o nº 1 está na lista
print(1 in numeros)

#se a intenção é fazer uma pesquisa na lista "numeros", podemos tornar a lista num set, que já excluir as duplicidades
numero = set[1,2,3,4,1,1,1,1,7,8,9]
print(numero)
#para verificar se o nº 5 está no set
print(5 in numero)

#Quando não usar set = quando quero manter a lista e a usa ordem ou quando quero itens duplicados
#Set não garante a ordem dos dados, por isso não se pode acessar determinado índice da set (muda sempre)

