# Depois de instalar pacotes, salve as dependências:
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push#!/usr/bin/env python3
print("Hello world!")

#para transformar tudo em maiúsculo
print('vanessa'.upper())

#para transformar somente a 1ª letra maiúscula
print('vanessa'.capitalize())

""" Comentário multi linhas
Documentação do código
Hello World Multi Línguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem 
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada,
Exemplo:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Vanessa Hillesheim"
__license__ = "Unlicense"

#Dunder é um idenditicador do python, para declarar que uma plavra está posta entre 2 underlines no ínicio e 2 underlines no final
#Dunder version  = __version__

import os

current_language = os.getenv("LANG", "en_US")[:5]
#para alterar a língua, no terminal:  export LANG=pt_BR.utf8

msg = "Hello, world!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg == "Cia, Mondo!"
elif current_language == "es_SP":
    msg == "Hola, Mundo!"
elif current_language == "fr_FR":
    msg == "Bonjour Monde!"

print(msg)