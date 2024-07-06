op = "a"
quantidade = 0
saques = 0.0
dinheiro = 0.0
operacoes = []
while op!="0":
    op = input("Escolha o que deseja fazer:\n[0] - Sair do programa\n[1] - Depositar dinheiro\n[2] - Sacar\n[3] - Extrato\n:")
    if(op=="1"):
        quantidade = float(input("Qual a quantidade a ser depositada: "))
        if (quantidade <= 0):
            print("Não tem como depositar um valor negativo")
        else:
            dinheiro += quantidade
            operacoes.append(quantidade)
            print("Valor depositado com sucesso")
    elif(op=="2"):
        quantidade = float(input("Qual a quantidade a ser sacada: "))
        if(saques < 3):
            if(quantidade > 500 or quantidade > dinheiro) or quantidade <= 0:
                print("Não foi possivel sacar o dinheiro")
            else:
                operacoes.append(-quantidade)
                saques += 1
                dinheiro -= quantidade
        else:
            print("Ja realizou o numero maximo de saques de hoje")
    elif(op=="3"):
        for i in operacoes:
            if(i>0):
                print(f"Foi realizado um deposito de R${i}")
            else:
                print(f"Foi realizado um saque de R${i}")
        print(f"Valor final na conta {dinheiro}")