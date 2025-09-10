#!/usr/bin/env python3

#OUTPUT é uma função de saída, com método write
#print é uma função que exibe a execução do comando
#se quiser que o resultado do print seja exibido num arquivo externo, é possível:
print(f"Hello world", file=open("hello.text", "a"))
#assim é aberto, no modo append, o arquivo hello.txt e tudo o que for printado vai para esse arquivo
print("olá", file=open("hello.text", "a"))

#INPUT é uma função de entrada, com método read
#sempre que precisamos de interação do usuário, forçando-o a preencher informações
nome = input("Qual é seu nome?")
print(nome)

#toda vez q se lê um dado recebido por input, ele vem como texto=string
#se a intenção é recer um inteiro do usuário, preciso configurar o input
idade = int(input("Qual a sua idade?"))
print(idade)

#a entrada de input sempre será texto, mas considera espaços em branco.
#para eliminar espaços em branco no começo e final do dado recebido, precisa utilizar a função .strip()

sobrenome = input("Qual é seu sobrenome?").strip()
print(sobrenome)