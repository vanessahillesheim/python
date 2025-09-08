#!/usr/bin/env python3

#Cadastro de Produto
__version__ = "0.1.0"

from pprint import pprint

produto = {
"nome":"Caneta",
"cores":["azul", "branco"],
"preco":3.23,
"dimensao": {
    "altura":12.1,
    "largura": 0.8,
},
"em_estoque": True,
"codigo": 45678,
"codebar": None,
}

cliente = {
    "nome": "Vanessa"
}

compra = {
    "clientes": cliente,
    "produto": produto, 
    "quantidade": 3
}


#como fazer para exibir para o cliente sua compra
#pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]
print(
    f"O cliente {compra['clientes']['nome']}"
    f" comprou {compra["quantidade"]} {compra["produto"]["nome"]}(s)"
    f" e pagou o total de R${total_compra}."
)