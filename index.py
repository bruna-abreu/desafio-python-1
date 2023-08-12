menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor = float(input("Digite o valor que você quer depositar: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Operação inválida! O valor informado não é aceito.")

    elif opcao == "s":
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor que deseja sacar: R$"))

            if valor <= saldo:
                
                if valor <= limite:
                    print(f"Saque de R${valor:.2f} realizado com sucesso")
                    numero_saques += 1
                    saldo -= valor
                    extrato += f"Saque de R${valor:.2f}\n"
                else:
                    print(f"O valor do saque excede o limite de R${limite:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")

        else:
            print("Você atingiu o limite de saques diários.")

    elif opcao == "e":
        print("\n============ EXTRATO ============\n")
        print(extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
