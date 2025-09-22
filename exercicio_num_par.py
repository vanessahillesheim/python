#!/usr/bin/env python3
"""
Faça um programa que imprima os números pares de 1 a 200.
"""

numeros = range(1,201)

for numero in numeros:
    par = numero %2 == 0
    if par:
        print(numero)

#resolução do professor
for num in range(1,201):
    if num %2 != 0:
        continue
    print(num)
    