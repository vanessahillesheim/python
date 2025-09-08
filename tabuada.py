#!/usr/bin/env python3
"""Imprime a tabuada de 1 ao 10.
Tabuada do 1
1
2
3
...
--------
Tabuada do 2
2
4
....
--------
"""

__version__ = "0.0.0"
__autora__ = "Vanessa"

"""
#base = [1,2,3,4,5,6,7,8,9,10]
#podemos usar o range para utilizar um intervalo de dados
#base = [1,2,3,4,5,6,7,8,9,10] => base = list(range(1,11))
#base = list(range(1,11))

numeros = list(range(1,11))
#Itarable = protocolo python para objeto "percorrível"
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-------------")

# unicode = Tabela ASCII + caracteres especiais
# utf8
# posso copiar um emotion da tabela Uncode (do google) e encodar
flower = "🌻"
flower_enconded = flower.encode("utf-8")

print(flower)


#Sliceable = fatiamento de objeto Python
nome = "Vanessa"
print(nome)

nome.__getitem__(3)
"""
#formatando a tabuada


numeros = list(range(1,11))

for n1 in numeros:
    print("{:^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1*n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)
  

