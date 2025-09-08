#!/usr/bin/env python3
"""
Exibir relatório de crianças por atividade extra curricular.
Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades.
"""
__version__ = "0.1.00"

sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Lola"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica),
    ("Dança",aula_danca)]

#listar alunos em cada atividade por sala 

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 43)
    
    atividade_sala1 = []
    atividade_sala2 = []
   
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print("-" * 43)
    print()