#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis para alugar e o preço
do quarto. Esta infotmação está disponível em um arquivo de texto separado por vírgulas.

'quarto.txt'
#código, nome, preço
1, suíte master, 500
2, quarto família, 200
3, quarto singre, 100
4, quarto sumples, 50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar a escolha em outro arquivo contendo as reservas

'reservas.txt'
#cliente, quarto, dias
Vanessa, 3, 5

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma mensagem informando que já está reservado.

"""
"""
import os

# Arquivos de dados
QUARTOS_FILE = 'quartos.txt'
RESERVAS_FILE = 'reservas.txt'

def carregar_quartos():
    #carrega a lista de quartos disponíveis do arquivo
    quartos = {}
    try:
        with open(QUARTOS_FILE, 'r', encoding='utf-8') as file:
            for linha in file:
                linha = linha.strip()
                if linha.startswith('#') or not linha:
                    continue  # Pula linhas de comentário ou vazias
                codigo, nome, preco = linha.split(',')
                quartos[codigo.strip()] = {
                    'nome': nome.strip(),
                    'preco': float(preco.strip()),
                    'disponivel': True
                }
        return quartos
    except FileNotFoundError:
        print(f"Erro: Arquivo '{QUARTOS_FILE}' não encontrado!")
        return {}
    except Exception as e:
        print(f"Erro ao carregar quartos: {e}")
        return {}

def carregar_reservas():
    #Carrega as reservas existentes do arquivo
    reservas = {}
    try:
        if os.path.exists(RESERVAS_FILE):
            with open(RESERVAS_FILE, 'r', encoding='utf-8') as file:
                for linha in file:
                    linha = linha.strip()
                    if linha.startswith('#') or not linha:
                        continue
                    cliente, quarto, dias = linha.split(',')
                    reservas[quarto.strip()] = {
                        'cliente': cliente.strip(),
                        'dias': int(dias.strip())
                    }
        return reservas
    except Exception as e:
        print(f"Erro ao carregar reservas: {e}")
        return {}

def salvar_reserva(cliente, quarto, dias):
    #Salva uma nova reserva no arquivo
    try:
        with open(RESERVAS_FILE, 'a', encoding='utf-8') as file:
            file.write(f"{cliente}, {quarto}, {dias}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar reserva: {e}")
        return False

def exibir_quartos_disponiveis(quartos, reservas):
    #Exibe a lista de quartos disponíveis
    print("\n" + "="*50)
    print("QUARTOS DISPONÍVEIS PARA RESERVA")
    print("="*50)
    print(f"{'Código':<10} {'Nome':<20} {'Preço/dia':<15} {'Status':<10}")
    print("-"*50)
    
    for codigo, info in quartos.items():
        status = "DISPONÍVEL" if codigo not in reservas else "RESERVADO"
        if status == "DISPONÍVEL":
            print(f"{codigo:<10} {info['nome']:<20} R$ {info['preco']:<12.2f} {status:<10}")
    
    print("="*50)

def main():
    # Carregar dados
    quartos = carregar_quartos()
    if not quartos:
        print("Não foi possível carregar os quartos. Verifique o arquivo 'quarto.txt'")
        return
    
    reservas = carregar_reservas()
    
    # Exibir quartos disponíveis
    exibir_quartos_disponiveis(quartos, reservas)
    
    # Solicitar dados do usuário
    print("\nFAZER RESERVA")
    print("-"*30)
    
    try:
        nome = input("Digite seu nome: ").strip()
        if not nome:
            print("Nome não pode estar vazio!")
            return
        
        codigo_quarto = input("Digite o código do quarto desejado: ").strip()
        
        # Verificar se o quarto existe
        if codigo_quarto not in quartos:
            print("Código de quarto inválido!")
            return
        
        # Verificar se o quarto já está reservado
        if codigo_quarto in reservas:
            reserva_existente = reservas[codigo_quarto]
            print(f"\n❌ Este quarto já está reservado para {reserva_existente['cliente']} por {reserva_existente['dias']} dias!")
            return
        
        # Solicitar quantidade de dias
        dias = int(input("Quantidade de dias: "))
        if dias <= 0:
            print("A quantidade de dias deve ser maior que zero!")
            return
        
        # Calcular valor total
        preco_diaria = quartos[codigo_quarto]['preco']
        valor_total = preco_diaria * dias
        
        # Exibir resumo da reserva
        print("\n" + "="*50)
        print("RESUMO DA RESERVA")
        print("="*50)
        print(f"Cliente: {nome}")
        print(f"Quarto: {quartos[codigo_quarto]['nome']} (Código: {codigo_quarto})")
        print(f"Dias: {dias}")
        print(f"Preço por dia: R$ {preco_diaria:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")
        print("="*50)
        
        # Confirmar reserva
        confirmacao = input("\nConfirmar reserva? (s/n): ").strip().lower()
        
        if confirmacao == 's':
            # Salvar reserva
            if salvar_reserva(nome, codigo_quarto, dias):
                print("✅ Reserva realizada com sucesso!")
                print(f"Arquivo '{RESERVAS_FILE}' atualizado.")
            else:
                print("❌ Erro ao salvar reserva!")
        else:
            print("Reserva cancelada.")
            
    except ValueError:
        print("Erro: Digite um valor numérico válido para dias!")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
"""

#RESOLUÇÃO DO PROFESSOR

# o quarto estará disponível quanto não estiver no reservas.txt e estiver no quartos.txt
import sys
import logging
import os

ocupados = {}
try: 
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome, 
            "dias": dias
                   }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe.")
    sys.exit(1)


quartos = {}
try: 
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome, 
            "preco": float(preco.strip()), 
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe.")
    sys.exit(1)



print("Reserva Hotel Pythônico")    
print("-" * 40)

if len(ocupados) == len(quartos):
    print("Hotel lotado!")

nome = input("Nome do cliente:").strip()
print("-" * 40)

print("Lista de quartos disponíveis")

for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco= dados["preco"]
    disponivel = "❌" if not dados['disponivel'] else "👍" #win + . abre o seletor de emojis
    print(f"{codigo} - {nome_quarto} - R${preco:.2f} - {disponivel}")


try:
    num_quarto = int(input("Número do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)    
except ValueError:
    logging.error("Número inválido. Digite apenas números.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")

try:
    dias = int(input("Quantos diárias?").strip())
except ValueError:
    logging.error("Número inválido. Digite apenas números.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

#depois que o cliente reserva, os comandos abaixo registar a reserva no arquivo txt
with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")
    file_.flush()  # Força a escrita imediata


print(f"{nome}, você escolheu o {nome_quarto} e vai custar R${total:.2f}.")