menu = """
***********************************
        
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

***********************************
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Infirme o valor do depósito: "))

        if valor > 0:
            saldo  += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação invalida! o valor informado é negativo.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação invalida! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação invalida! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação invalida! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação invalida! O valor informado é negativo")

    elif opcao == "3":
        print ("\n########### Extrato ###########\n")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###############################")
        
    elif opcao == "4":
        break

    else:
        print ("Opção inváida, selecione a opção correta.")

