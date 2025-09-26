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

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# Acesso ao banco de dados

# TODO: Usar pacote csv

ocupados = {}  # acumulador
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": int(dias),
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)


# TODO: Usar função para ler os arquivos

quartos = {}  # acumulador
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco),  # TODO: Usar Decimal
            "disponivel": False if int(num_quarto) in ocupados else True,
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)

# Programa principal
print("Reservas no Hotel Pythonico da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel está lotado, volte depois.")
    sys.exit(0)

nome_cliente = input("Qual é o seu nome:").strip()
print()

# TODO: Usar rich.Table
print("Lista de quartos")
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "⛔" if not dados_quarto["disponivel"] else "👍"
    print(
        f"{num_quarto:<6} - {nome_quarto:<14} - " f"R$ {preco:<9.2f} - {disponivel:<10}"
    )

print("-" * 52)
# reserva

try:
    num_quarto = int(input("Qual o quarto desejado:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro.")
        sys.exit(0)
except KeyError:
    print(f"O Quarto {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    print("Número inválido, digite apenas digitos.")
    sys.exit(0)

try:
    dias = int(input("Quantos dias:").strip())
except ValueError:
    print("Número inválido, digite apenas digitos.")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(
    f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} "
    f"o valor total estimado será R$ {total:.2f}"
)

if input("Confirma? (digite y)").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")