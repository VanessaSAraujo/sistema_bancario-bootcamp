saldo = 0
limite = 500
LIMITE_SAQUES = 3
numero_saques = 0
extrato = ""


while True:
    print("\n--- Menu do Sistema Bancário ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor para depositar: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação negada! Insira um valor válido.")
    elif opcao == '2':
        valor = float(input("Digite o valor para sacar: R$ "))

        if valor > 0:
            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques excedido.")
            elif valor > saldo:
                print("Saldo insuficiente")
            elif valor > limite:
                print("Valor acima do limite diário permitido.")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    elif opcao == '3':
        if extrato:
            extrato_completo = f"""
{extrato}
Saldo atual: R$ {saldo:.2f}
"""
            print(extrato_completo)
        else:
            print("Não foram realizadas movimentações.")
    
    elif opcao == '0':
        print("Saindo do Sistema")
        break

    else:
        print("Opção inválida! Tente novamente.")