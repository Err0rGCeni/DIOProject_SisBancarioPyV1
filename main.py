menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

LIMITE_SAQUES = 3
saldo = 0
limite = 500
extrato = ""
n_saques = 0
saques_realizados = []

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor a depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor de depósito inválido!")

    elif opcao == 's':
        if n_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a sacar: "))
            if valor_saque <= limite and valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                saques_realizados.append(valor_saque)
                n_saques += 1
            else:
                print("Valor de saque excede o limite ou saldo insuficiente!")
        else:
            print("Limite de saques diários atingido!")

    elif opcao == 'e':
        if extrato:
            print("Movimentações:\n" + extrato + f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == 'q':
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
