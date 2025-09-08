#!/usr/bin/env python3

# interpolação = usando placeholder

template = "O saldo do %s é o total de R$%d."

nome = "Vanessa"
saldo = 30

resultado = template % (nome, saldo)
print(resultado)

#vários dados, usando placeholder com etiqueta
#s = string,  d = dígito/número f= float, 2f = 2 casas decimais
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

#old style = usando %
msg = "Olá %s, você é o player nº %03d e você tem %.5f pontos!"
player = "John"
numero = 15
pontos = 3725

mensagem = msg % (player, numero, pontos)
print(mensagem)

#New style = usando .format e {}
msg = "Olá {}, você é o player nº {:03d} e você tem {:.5f} pontos!"
player = "John"
numero = 15
pontos = 3725

mensagem = msg.format(player, numero, pontos)
print(mensagem)

#str format
#centralizando o texto dentro de 20 caracteres
formatando = "{:^20}".format("Vanessa")
print(formatando)

#Alinhando à esquerda
formatando = "{:<20}".format("Vanessa")
print(formatando)

#Alinhando à direita
formatando = "{:>20}".format("Vanessa")
print(formatando)

#Alinhando à direita e preenchendo com -
formatando = "{:->20}".format("Vanessa")
print(formatando)

#centralizando o texto dentro de 20 caracteres e preenchendo os espaços laterais com *
formatando = "{:*^20}".format("Vanessa")
print(formatando)

#centralizando o texto dentro de 20 caracteres e preenchendo os espaços laterais
# com # e exibindo apenas 3 primeiros caracteres
formatando = "{:#^20.3}".format("Vanessa")
print(formatando)

#centralizando o texto dentro de 20 caracteres e preenchendo os espaços laterais
# com # e exibindo apenas 3 primeiros caracteres
formatando = "{:#^20.3}".format("Vanessa")
print(formatando)

#f string
# assim não precisamos colocar .format... só o f"string" resolve
name = "João"
saldo = 200000

saudacao = f"Olá {name}! Você tem R${saldo:.2f} de saldo na conta correte"
print(saudacao)

# f-string com formatação mais clara
name = "João"
saldo = 200000

# Formata em dólar e depois converte para formato brasileiro
valor_formatado = f"R${saldo:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
saudacao = f"Olá {name}! Você tem {valor_formatado} de saldo na conta corrente"
print(saudacao)

"""
#%S concatenação = usar quando usar bibiloteca logging
#srt.format {} = usado em mensagens logas: e-mails
#f-strings = usado em todo o restante
"""

#como imprimir emoji no python
# nas tabelas de emojis existe o código de cada um
# para imprimir panda
print("\U0001F43C")
print("\U0001F600")

#python tbém permite fazer a busca pelo nome do emoji
print("\N{panda face}")
print("\N{green apple}")
