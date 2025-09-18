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
#com logging
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Vanessa", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
       log.error(
           "Você precisa ditigar '=', você usou %s, tente --key=value: %s", 
           arg, 
           str(e)
       )
       sys.exit()

    key = key.lstrip("-").strip()
    value = value.strip()

#validação
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Escolha a linguagem:")


#fazendo o fatiamento
current_language = current_language[:5]

msg = {
    "en_US": "Hello, world!", 
    "pt_BR": "Olá, Mundo!", 
    "it_IT": "Cia, Mondo!", 
    "es_SP": "Hola, Mundo!", 
    "fr_FR":"Bonjour Monde!",
}

#para alterar a linguagem, no terminal devo digitar:
#python hello_sys.py --lang=it_IT 

#EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Linguagem é invalida (não está nos 5 idiomas do dicionário). Escola um dos idiomas: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
