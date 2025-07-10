saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def menu():
 '''
######## MENU ###########
      
  [d]- Depositar       [e]- Extrato
  [s]- Saque           [c]- Criar conta corrente
  [u]- criar usuario   [q]- Sair
  [l]-listar contas
  
#########################
  escolha uma opção  
    '''
 return input(menu)

def deposito (saldo, valor, extrato, /):  
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
        else:
             print("Deposito não realizado, verifique as condições e tente novamente!")
        return saldo, extrato     

def saque (*saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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
            print("Saque realizado com sucesso!")
        else:
            print("A operação é invalida, por favor tente novamente!")
        
        return saldo, extrato
   
   
def exibir_extrato (saldo,/,*,extrato):
        print("\n######## EXTRATO ###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#########################")

def criar_usuario(usuarios):
   cpf = input("Digite seu cpf (somente numeros): ")
   usuario = filtro_usuario(cpf, usuarios)

   if usuario:
        print("Ja existe usuario com esse numero de cpf")
        return
 
   nome = input("Digite seu nome completo: ")
   data_nasc = input("Digite sua data de nascimento (dd-mm-aa): ")
   endereco = input("Informe o seu endereço (Logradouro, nro - Bairro - Cidade/Sigla  estado): ")

   usuario.append({"Nome":{nome}, "Data de Nascimento": {data_nasc},"CPF": {cpf}, "Endereço":{endereco}})

   print("Usuario cadastrado com sucesso!")
   

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados  = [usuario for usuario in usuarios if usuario ["CPF" == cpf]]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta_corrente(AGENCIA, numero_conta, usuarios):
    cpf = input("Digite seu cpf (somente numeros): ")
    usuario = filtro_usuario(cpf, usuarios)
   
    if usuario:
         print("Conta criada com sucesso!")
         return {"Agencia": AGENCIA, "Numero da conta": numero_conta, "Usuario": usuario}



def listar_contas(contas):
    for conta in contas:
         linha = f"""\
              Agencia:{conta['AGENCIA']}
              C/C: {conta['numero_conta']}
              Titular: {conta['usuario']['nome']}
          """
         print("a" * 100)
         print(linha)



while True:
     opcao = menu()

     if opcao == "d":
          valor = float(input("Digite o valor de deposito: "))

          saldo, extrato = deposito( saldo, valor, extrato)

     elif opcao == "s":
          valor = float(input("Digite o valor de saque: "))
     
     elif opcao == "e":
          exibir_extrato(saldo, extrato=extrato)

     elif opcao == "u":
          criar_usuario(usuarios)

     elif opcao == "c":
          numero_conta = len(contas) + 1
          
          conta = criar_conta_corrente(AGENCIA , numero_conta, usuarios)
          
          if conta:
           contas.append(conta)
    
     elif opcao == "l":
          listar_contas(contas)
     
     elif opcao == "q":
          break
     
     else:
          print("Opcção invalida, tente utilizando alguma opção valida!")

