#!/usr/bin/env python3

#Cadastro de Produto
__version__ = "0.1.0"

""" exemplo sem uso de dicionário

produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None

compra = ("Bruno", produto_nome, 3)
#como fazer para exibir para o cliente sua compra
total_compra = compra[2] * produto_preco
print(f"O cliente {compra[0]} comprou {compra[1]} e pagou o total de R${total_compra}.")
"""

#ainda usando listas []
atividades = [
    ("Inglês", ["João", "Maria"]), 
    ("Música", ["João", "Sofia"])
    ]
#para imprimir a 1ª posição do dicionário
print(atividades[0])

for atividade in atividades:
    if atividade[0] =="Música":
        print(atividade[1])
#O(n) essa operação fica tão complexa como o tamanho da lista

#Usando dicionário
#Dicionário usa set e lista, é mutável e iterável
#Dicionario tem característica de set, não permite chave duplicada e atualiza o valor (só mantem a últmia)
#Dicionário guarda duas informações (chave e valor) por posição (diferente da lista que só guarda um valor por posição)
#Dicionários são criados entre {}

cliente = {"nome": "Vanessa", "cod.": 123, "cidade": "Curitiba"}
#para adicionar item ao dicionario
cliente.update({"estado":"PR"})
print(cliente)

#como pesquisar uma chave no dicionario
pesquisa = "cod." in cliente
print(pesquisa)

#exibir a chave nome, tornar tudo maiúsculo e substituir o V por W
print(cliente["nome"].upper().replace("V", "W"))

#para apagar item do dicionario
del cliente["nome"]
print(cliente)

#para saber o tamanho do dicionário
print(len(cliente))

#criando outro dicionário com informação extra e unindo-os
extra = {"sobrenome":"Hillesheim"}

cadastro = {**cliente, **extra}
print(cadastro)


#para acessar as chaves de um dicionário
for chave in cadastro:
    print(chave)
print("--------------------")

#para acessar a chave e o valor de um dicionário
for chave in cadastro:
    print(chave, "->", cadastro[chave])
print("--------------------")

#para acessar a chave e o valor de um dicionario (de outra forma)
for chave, valor in cadastro.items():
    print(chave, "->", valor)
print("--------------------")
