#!usr/bin/env python3

#WHILE opera em cima de uma condição
#enquanto uma condição for verdadeira, repita o loop

#condição da parada (exibir os números, começando em 0 até 99)
n = 0
while n < 100: 
    print(n)
    n += 1

#condição da parada (exibir os números, começando em 0 até 99, mas parando se for igual a 40)
n = 0
while n < 100: 
    if n == 40:
        break
    print(n)
    n += 1

#condição da parada (exibir os números, começando em 0 até 99, mas pulando se for igual a 40)
n = 0
while n < 100:
    if n == 40:
        n += 1 #tem q colocar o incremento, pq se não vai travar voltando para o início
        continue
    print(n)
    n += 1

#condição da parada (exibir os números, começando em 0 até 99, mas pulando de 40 a 60)
n = 0
while n < 100:
    if n >= 40 and n <= 60:
        n += 1 
        continue
    print(n)
    n += 1

#condição da parada (exibir os números, começando em 0 até 99, quando for par)
n = 0
while n < 100:
    if n % 2 == 0:      # Se for par, imprime
        print(n)
    n += 1              # Sempre incrementa

#condição da parada (exibir os números, começando em 0 até 99, quando for par)
n = 0
while n < 100:
    if n % 2 != 0:      
        n +=1
        continue
    print(n)
    n += 1              