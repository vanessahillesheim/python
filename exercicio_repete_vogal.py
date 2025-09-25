#!/usr/bin/env python3
"""
Repete Vogais

Faça um programa que pede ao usuário que digite uma ou mais palavrsaa e imprime cada uma das palavras com suas vogais duplicadas.

Exemplo:
'Digite uma palavra (ou enter para sair)': Python
'Digite uma palavra (ou enter para sair)': Vanessa
'Digite uma palavra (ou enter para sair)': <enter>
Pythoon
Vaaneessaa
"""

'''
import logging
import sys
log = logging.Logger ("alerta")

vogais = "aeiouAEIOU"
palavras = []


while True:
    try:
        palavra = input("Digite uma palavra (ou enter para sair):").strip()
        #se o usuário digitar  enter (string vazia), sai do log
        if palavra == "":
            break

        palavras.append(palavra)
    
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        sys.exit(0)
    
    except Exception as e:
        log.error(f"Erro na digitação {e}")
        continue

#Processa cada palavra digitada
for palavra in palavras:
    nova_palavra = ""

    #para cada caractere na palavra
    for letra in palavra:
        #se for vogal, duplica
        if letra in vogais:
            nova_palavra += letra*2
        else:
            nova_palavra += letra
    print(nova_palavra)
'''

#Resolução do professor

palavras = []
while True:
    palavra = input("Digite uma palavra (ou enter para sair):").strip()
    if not palavra: # se não ditigar nada, para
        break

    nova_palavra = ""
    
    for letra in palavra:
        if letra in "aeiouAEIOUãÃíÍóÓõÕáÁúÚêêôÔõÕ":
            nova_palavra += letra*2
        else:
            nova_palavra += letra
    palavras.append(nova_palavra)

#desempacotar com * separar com traço
print(*palavras, sep="\n")