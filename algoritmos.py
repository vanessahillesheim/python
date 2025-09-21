#Algoritmos
#Sequência de instruções lógicas que visam obter a solução de um problema.

'''
Statements (não retorna valor = executam ações):
-Se -> if
-Senão, se -> elif (else if)
-Senão -> else

Operadores Lógicos
-E -> and
-Ou -> or
-Não -> not

Assignments (guarda um valor)
A padaria está aberta? (boleano: True/False)

Expressions (quando se espera uma resposta True ou False)

# Assignment
idade = 20
tem_ingresso = True
eh_estudante = False

# Expression + Statements
if idade >= 18 and tem_ingresso:
    print("Pode entrar!")
    if eh_estudante:
        print("Tem direito a desconto!")
elif idade >= 18 and not tem_ingresso:
    print("Compre um ingresso primeiro")
else:
    print("Menor de idade não pode entrar")
'''

#PSEUDO CÓDIGO PARA IR COMPRAR PÃO NA PADARIA
'''
import ir, pegar, pedir, tem, comer, ficar

Premissas:
today = "segunda"
hora = 15
natal = False
chovendo = True
frio - True
nevando = True
semana = ["segunda", "terça", "quarta", "quinta", "sexta"]
feriado = ["quarta"}
horario_padaria = {
    "semana": 19, 
    "findi": 12
}

Algoritmo
1) decidir se a padaria está ou não aberta
if today in feriados and not natal:
    padaria_aberta = Fale
elif today not in semana and hora < horario_padaria["findi"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

2) padaria aberta E:
if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda_chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda_chuva")
        pegar("agua")
    elif:
         pegar("guarda_chuva")
   

3) ir até a padaria (executar a função)
    ir("padaria")

    if tem("pao_integral") and tem("massinha"):
        pedir(6, "pao_integral")
        pedir(6, "massinha")
    elif tem("pai_integral") or tem("massinha):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer coisa")

else:
    ficar("casa")
    comer("bolacha")

'''