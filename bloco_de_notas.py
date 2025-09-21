#!/usr/bin/env python3
"""Bloco de Notas

$ bloco_de_notas.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreita de tecnologia

$ bloco_de_notas.py read tech
...
...

# Execute o arquivo
python bloco_de_notas.py new "título da Nota"

"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")


arguments = sys.argv[1:]
if not arguments:
    print("Uso inválido")
    print(f"você deve especificar um comando: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Comando inválido {arguments[0]}")
    sys.exit(1)

#fazer um loop para o usuário continuar postando sem ter q executar novamente
while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()

        #leitura das notas
        for line in open(filepath):
            titulo, tag, texto = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"titulo: {titulo}")
                print(f"texto: {texto}")
                print("-" *30)
                print()

    if arguments[0] == "new":
        try:
            titulo = arguments[1]
        except IndexError:
            titulo = input("Qual é o título?").strip().title()

        texto = [
            f"{titulo}", 
            input("tag:").strip(),
            input("texto:\n").strip(),
            
        ]
    #\t - tsv
        with open(filepath, "a") as file_:
           file_.write("\t".join(texto) + "\n")
    
    continuar = input(f"Quer continuar {arguments[0]} notas? [n/y]").strip().lower()
    if continuar != "y":
            break
       
