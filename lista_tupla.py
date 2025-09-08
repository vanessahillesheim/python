#!/usr/bin/env python3

#OBJETOS COMPOSTOS
## TUPLAS

# essa é uma tupla, que é IMUTÁVEL. Tem um índice e um valor: 0:Bruno; 1:15; 2:True; 3:None; 4:45.3
# pode usar parenteses ou não
dados = "Bruno", 15, True, None, 45.3

#contar qtos "Brunos" tem em dados
print(dados.count("Bruno"))

#contar qtos "bananas" tem em dados
print(dados.count("banana"))

#exibir o último elemento de dados
print(dados[-1])

#exibir o 4º elemento de dados (lembrando que começa em zero)
print(dados[4])

#desempacotamento de tupla

pontos = (2, 1, 99)
x, y, z = pontos

x, *resto = pontos
print(pontos)
print(pontos[2])

## LISTAS

# Listas são semelhantes a arrays. São objetos MUTÁVEIS
# lisas são criadas entre []

users = []

#adicionando elemento no final na lista users
users.append("Vanessa")
print(users)

#adicionando elemento no começo da lista
users.insert(0, "Ana Julia")
print(users)

#adicionando elemento no final na lista users
users.append("Pedro")
print(users)

#excluindo elemento da lista users
users.remove("Pedro")
print(users)

#adicionado uma outra lista à lista "users"
outros_users = ("Marcos", "Felipe")
users.extend(outros_users)
users += ["Maria"]
print(users)

#pop exclui o último elemento da lista
print(users.pop())
print(users.pop())
print(users)

#iterações com lista
resultado = []
for x in range(9):
    resultado.append(x * 4)
print(resultado)