#!/usr/bin/env python3

"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o ínidice de umidade do ar.
Deverá ser exibida mensagem de alerta, dependendo das condições:

temperatura maior 45: ALERTA! Perigo calor extremo;
temperatura vezes 3 for maior ou igual a umidade: ALERTA! Perigo de calor úmido
temperatura entre 10 e 30: Normal
temperatura entre 0 e 10: Frio
temperatura <0: Frio extremo
"""

temp = float(input("Qual a temperatura atual?").strip())
umidade = float(input("Qual a umidade do ar atual?").strip())

if temp >45:
    print(f"Com a temperatura de {temp:.2f} graus é considerado 'calor extremo'.")
elif (temp *3) >= umidade:
     print("ALERTA: Perigo de calor úmido")
elif temp >=10 and temp <=30:
    print(f"A temperatura de {temp:.2f} graus é considerada 'normal'.")
elif temp >=0 and temp <10:
    print(f"A temperatura de {temp:.2f} grau(s) é considerada 'fria'.")
else:
     print(f"Com a temperatura de {temp:.2f} grau(s) é considerado 'frio extremo'.")



#resolução do professor
import logging
import sys
log = logging.Logger ("alerta")

try:
    temp = float(input("Qual a temperatura atual?").strip())
except ValueError:
    log.error("Temperatura inválida!")
    sys.exit(1)

try:  
    umidade = float(input("Qual a umidade do ar atual?").strip())
except ValueError:
    log.error("Umidade inválida!")
    sys.exit(1)


if temp >45:
    print(f"Com a temperatura de {temp:.2f} graus é considerado 'calor extremo'.")
elif (temp *3) >= umidade:
     print("ALERTA: Perigo de calor úmido")
elif temp >=10 and temp <=30:
    print(f"A temperatura de {temp:.2f} graus é considerada 'normal'.")
elif temp >=0 and temp <10:
    print(f"A temperatura de {temp:.2f} grau(s) é considerada 'fria'.")
elif temp <0:
     print(f"Com a temperatura de {temp:.2f} grau(s) é considerado 'frio extremo'.")