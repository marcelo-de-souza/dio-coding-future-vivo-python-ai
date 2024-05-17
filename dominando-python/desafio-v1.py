menu = """
    BANCO DIO
****** MENU ******

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

******************
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
opcao = ""

while opcao != "q":
    opcao = input(menu)

    if opcao == "d":        
        print("\nDéposito selecionado")
        deposito = float(input("\nDigite o valor do depósito: "))
        print()
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Déposito R$ {deposito:.2f}\n"
            print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
        else:
            print("Opção inválida. Operação de Depósito abortada!")
            

    elif opcao == "s":
        print("\nSaque selecionado")
        
        saque = float(input("Digite o valor do saque: "))

        if saque > 0:
        
            if numero_saques >= limite_saques:
                print("Limite de saques diário atingido. Saque não realizado!")
            
            elif saque > limite:
                print("Valor ultrapassa limite para saque unitário. \nSaque não realizado")
            
            elif saque > saldo:
                print("Saldo insuficiente. Operação cancelada!")
            
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                print(f"Seu saldo atual é: R$ {saldo:.2f}\n")

        
    elif opcao =="e":
        print("\nExtrato selecionado")
        print("\n========== EXTRATO ==========")
        print("Não há transações no período!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    
    else:
        print("Opção inválida. Tente novamente.")


else:
    print("O BANCO DIO agradece sua confiança!") 