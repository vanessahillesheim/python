#!/usr/bin/env python3
"""Bloco de Notas

$ bloco_de_notas.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreita de tecnologia

$ bloco_de_notas.py read tech
...
...
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

if arguments[0] == "read":
    #leitura das notas
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {titulo}")
            print(f"texto: {texto}")
            print("-" *30)
            print()

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}\n", 
        input("tag:").strip(),
        input("text:\n").strip(),
        "\n"
    ]
#\t - tsv
with open(filepath, "a") as file_:
    file_.write("\t".join(text) + "\n")