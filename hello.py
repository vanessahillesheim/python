#!/usr/bin/env python3

""" Depois de instalar pacotes, salve as dependências:
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push#!/usr/bin/env python3
print("Hello world!")
"""
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
print(f"LANG detectada: {current_language}")

"""
#para alterar a língua, no terminal: 
# Testar com Português
export LANG=pt_BR.UTF-8
python3 hello.py

# Testar com Espanhol
export LANG=es_ES.UTF-8
python3 hello.py

# Testar com Italiano
export LANG=it_IT.UTF-8
python3 hello.py

# Testar com Francês
export LANG=fr_FR.UTF-8
python3 hello.py

# Voltar para Inglês
export LANG=en_US.UTF-8
python3 hello.py
"""

#Ordem de complexidade O(n) = de acordo com a quantidade de testes (neste caso 5 líguas)
msg = "Hello, world!"
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Cia, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)

#Ordem de complexidade O(1) = sets (Hash table) deixa mais rápido, velocidade constante
import os
current_language = os.getenv("LANG", "en_US")[:5]
msg = {
    "en_US": "Hello, world!", 
    "pt_BR": "Olá, Mundo!", 
    "it_IT": "Cia, Mondo!", 
    "es_SP": "Hola, Mundo!", 
    "fr_FR":"Bonjour Monde!",
}
print(msg[current_language])