
#menu#

menu = '''

-------- Menu --------
[1] Saldo
[2] Deposito
[3] Saque
[4] Extrato
[0] Sair


'''
saldo = float(0)
limite = float(500)
extrato = ""
numero_saque = 0
limite_saque = 3
extrato_atual = []

while True:
    print (menu)
    entrada = input ("Escolha sua Opção: ")

    if entrada == "1":
        print (f"Seu Saldo é R$ {saldo:.2f}")


    elif entrada == "2":
        dp = float(input ("Digite Valor: "))
        saldo += dp
        extrato_atual.append(('deposito:', dp))
        print (f"Seu Saldo é R$ {saldo:.2f}")

    elif entrada == "3":
        sq = float(input ("Digite Valor: "))

        if sq <= saldo and sq <= limite and numero_saque <= limite_saque:
            saldo -= sq
            extrato_atual.append(('saque:', sq))
            numero_saque += 1
            print (f"Saque realizado com sucesso: R$ {sq:.2f}")
        elif sq > saldo:
            print ("Seu saldo é insuficiente")
        elif sq > limite:
            print ("O valor do saque superior ao seu limite")
        elif numero_saque >= limite_saque:
            print ("Limite de saque atigindo")

    elif entrada == "4":
        print (''' ----- Extrato ----- ''')
        if extrato_atual:
            for tipo, valor in extrato_atual:
                print (f"{tipo}: R$ {valor:.2f}")
        else:
            print ("Nenhuma movimentação realizada")

    elif entrada == "0":
        print (''' --- Obridgo ---
               
               Saindo do sistema...
               
               ''')       
        break
