from datetime import datetime


opcao = ''
saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
NUMERO_SAQUE_LIMITE = 3

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

            valor = float(input("Valor: R$"))

            saldo += valor

            print(f"O valor de R${valor} foi depositado em sua conta")

            extrato += f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                          } - Deposito de R${valor}\n"

            break

        elif opcao == "S":

            if numero_saque < NUMERO_SAQUE_LIMITE:

                valor = float(input("Valor: R$"))

                if saldo >= valor:
                    saldo -= valor
                    numero_saque += 1

                    print(f"Saldo no valor de R${
                          valor} foi sacado com sucesso.")

                    extrato += f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                  } - Saque de R${valor}\n"

                    break
                else:
                    print("Saldo insuficiente")
                    break
            else:
                print("Limite de saque excedido")

            break

        elif opcao == "E":
            print(f"Extrato: \n{extrato} \n \n Extrato gerado em: {
                  datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

            break
        elif opcao == "Q":
            break
        else:
            print("Opção inválida")
            break
