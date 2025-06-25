menu = '''
######## MENU ###########
      
  [d]- Depositar       [e]- Extrato
  [s]- Sacar           [q]- Sair

#########################
  escolha uma opção  
    '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Digite o valor do deposito: "))
        
        if valor > 0:
            
            saldo += valor 
            
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação é invalida, por favor tente novamente!")

    elif opcao == "s":

        valor = float(input("Digite o valor de saque: "))

        exedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
       
        if exedeu_saldo:
            print("Valor de saldo insuficiente para saque! Tente valor em saldo.")

        elif excedeu_limite:
            print("Excedeu o limite do saque! Reduza o valor e tente novamente.")
        
        elif excedeu_saques:
            print("Excedeu o limite de saques diários! Tente novamente amanhã.")  
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("A operação é invalida, por favor tente novamente!")

    elif opcao == "e":
        print("\n ######## EXTRATO ###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#########################")

    elif opcao == "q":
        break

    else:
        print("Operação Invalída! Tente novamente com uma opção disposta pelo banco.")




         
