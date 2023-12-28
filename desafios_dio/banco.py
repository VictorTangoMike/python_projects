from datetime import datetime


opcao = ''
saldo = 0
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
MAX_VALUE_SAQUE = 500

def saque(extrato, saldo, numero_saque):
    global LIMITE_SAQUE, MAX_VALUE_SAQUE
    
    if numero_saque < LIMITE_SAQUE:
        
        valor = float(input("Valor: R$"))

        if saldo >= valor:
            saldo -= valor
            numero_saque += 1
            print(f"O valor de R${valor} foi sacado com sucesso.")

            msg = f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - Saque de R${valor}\n"

            extrato += msg            
        else: 
            print("Saldo insuficiente")
    else:
        print(f"Limite de saque excedido")

    return extrato, saldo, numero_saque

def deposito(extrato, saldo):
    valor = float(input("Valor: R$"))

    saldo += valor

    print(f"O valor de R${valor} foi depositado em sua conta")

    msg = f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - Deposito de R${valor}\n"

    extrato += msg

    return extrato, saldo

while opcao != "Q":
    opcao = input("""
    -------- Menu --------

    D - Deposito
    S - Saque
    E - Extrato
    Q - Sair
    \n""").upper()

    print('\n')

    while True:
        if opcao == "D":

            extrato, saldo = deposito(extrato, saldo)

            break

        elif opcao == "S":

            extrato, saldo, numero_saque = saque(extrato, saldo, numero_saque)

            break

        elif opcao == "E":
            print(f"Extrato: \n{extrato} \n \n Extrato gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

            break
        elif opcao == "Q":
            break
        else:
            print("Opção inválida")
            break
