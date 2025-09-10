#!/usr/bin/env python3
"""
Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:
Tenha a variável LANG devidamente configurada 
    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar no input.

"""

__version__ = "0.0.1"
__author__ = "Vanessa Hillesheim"
__license__ = "Unlicense"

#Dunder é um idenditicador do python, para declarar que uma plavra está posta entre 2 underlines no ínicio e 2 underlines no final
#Dunder version  = __version__

import os
#alterando o arquivo Hello.py, para não precisar alterar a linguagem no terminal=variável de ambiente
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option Key")
        sys.exit()
    arguments[key] = value



current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Escolha a linguagem:")


current_language = current_language[:5]

msg = {
    "en_US": "Hello, world!", 
    "pt_BR": "Olá, Mundo!", 
    "it_IT": "Cia, Mondo!", 
    "es_SP": "Hola, Mundo!", 
    "fr_FR":"Bonjour Monde!",
}

#para alterar a linguagem, no terminal devo digitar:
#python hello_sys.py --lang=it_IT --count=5
print(msg[current_language] * int(arguments["count"]))