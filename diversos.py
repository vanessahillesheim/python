#!/usr/bin/env python3

# interpolação = usando placeholder

template = "O saldo do %s é o total de R$%d."

nome = "Vanessa"
saldo = 30

resultado = template % (nome, saldo)
print(resultado)

#vários dados, usando placeholder com etiqueta
#s = string,  d = dígito/número f= float
email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponíveis!
Preço promocional R$%(preco).2f.
"""

clientes = ["Vanessa", "Bruno", "Pedro"]

for cliente in clientes:
    print(email_tmpl
     % {
        "nome": cliente, 
        "produto": "caneta", 
        "texto": "escrever muito bem", 
        "link": "https://canetaslegais.com", 
        "quantidade": 1, 
        "preco": 50.5, 
     }
    )
