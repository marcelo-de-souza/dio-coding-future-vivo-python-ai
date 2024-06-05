<<<<<<< HEAD
import textwrap

def menu():
    menu = """
        BANCO DIO
    ****** MENU ******

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Cadastrar Conta
    [l] Listar Contas
    [q] Sair

    ******************
    => """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
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
        
        return saldo, extrato

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R$ {deposito:.2f}\n"
            print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
    else:
            print("Opção inválida. Operação de Depósito abortada!")
    
    return saldo, extrato

def emitir_extrato(saldo, /, *, extrato):
    print("\nExtrato selecionado")
    print("\n========== EXTRATO ==========")
    print("Não há transações no período!" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe seu número de CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
         print("Já existe usuário cadastrado com este CPF!")
         return

    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe seu endereço (Logradouro, nº - Bairro - Cidade-UF: )")

    usuarios.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereço})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta,usuarios):
     cpf = input("Informe CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuarios:
          print("Conta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print(" Usuário não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("-" * 100)
          print(textwrap.dedent(linha)) 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    opcao = ""
        

    while True:
        opcao = menu()

        if opcao == "d":        
            print("\nDéposito selecionado")
            deposito = float(input("\nDigite o valor do depósito: "))
            print()
            saldo, extrato = depositar(saldo, deposito, extrato)   

        elif opcao == "s":
            print("\nSaque selecionado")
        
            saque = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                 saldo=saldo,
                 saque=saque,
                 extrato=extrato,
                 limite=limite,
                 numero_saques=numero_saques,
                 limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            emitir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            cadastrar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            print("O BANCO DIO agradece sua confiança!")
            break

        else:
            print("Opção inválida. Tente novamente.")


    else:
        print("O BANCO DIO agradece sua confiança!")

=======
import textwrap

def menu():
    menu = """
        BANCO DIO
    ****** MENU ******

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Cadastrar Conta
    [l] Listar Contas
    [q] Sair

    ******************
    => """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
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
        
        return saldo, extrato

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R$ {deposito:.2f}\n"
            print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
    else:
            print("Opção inválida. Operação de Depósito abortada!")
    
    return saldo, extrato

def emitir_extrato(saldo, /, *, extrato):
    print("\nExtrato selecionado")
    print("\n========== EXTRATO ==========")
    print("Não há transações no período!" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe seu número de CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
         print("Já existe usuário cadastrado com este CPF!")
         return

    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe seu endereço (Logradouro, nº - Bairro - Cidade-UF: )")

    usuarios.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereço})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta,usuarios):
     cpf = input("Informe CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuarios:
          print("Conta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print(" Usuário não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("-" * 100)
          print(textwrap.dedent(linha)) 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    opcao = ""
        

    while True:
        opcao = menu()

        if opcao == "d":        
            print("\nDéposito selecionado")
            deposito = float(input("\nDigite o valor do depósito: "))
            print()
            saldo, extrato = depositar(saldo, deposito, extrato)   

        elif opcao == "s":
            print("\nSaque selecionado")
        
            saque = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                 saldo=saldo,
                 saque=saque,
                 extrato=extrato,
                 limite=limite,
                 numero_saques=numero_saques,
                 limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            emitir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            cadastrar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            print("O BANCO DIO agradece sua confiança!")
            break

        else:
            print("Opção inválida. Tente novamente.")


    else:
        print("O BANCO DIO agradece sua confiança!")

>>>>>>> 3ce25b4 (envio desafio-v3.py)
main()