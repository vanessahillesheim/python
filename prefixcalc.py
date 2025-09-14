#!/usr/bin/env/python3

"""
Funcionamento:
[Operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
siv -> /

Uso:
$prefixcalc.py sum 5 2
7
$prefixcalc.py mum 10 5
50
$preficalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ ="0.1.0"

import sys
arguments = sys.argv[1:]


if not arguments:
    operacao = input("digite a operação:")
    n1 = input("Digite o primeiro número:")
    n2 = input("Digite o segundo número:")
    arguments = [operacao, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos.")
    print("Ex: 'sum 4 5'")
    sys.exit(1)
operacao, *nums = arguments

valida_operacoes = ("sum", "sub", "mul", "div")
if operacao not in valida_operacoes:
    print("Operação inválida.")
    print(valida_operacoes)
    sys.exit(1)

valida_numeros = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valida_numeros.append(num)

n1, n2 = valida_numeros

#TODO: Usar dicionário de Funções
if operacao == "sum":
    resultado = n1+n2
elif operacao == "sub":
    resultado = n1-n2
elif operacao == "mul":
    resultado = n1*n2
elif operacao == "div":
    resultado = n1/n2

print(f"O resultado é {resultado}")


