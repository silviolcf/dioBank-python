extrato = []
saldoTotal = 0
saida = False
saquesTotal = 0



while (saida == False):
    print("Escolha uma operação")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    operacao = int(input(">>>"))
    if operacao == 1:
        print("Informe o valor do deposito")
        valor = float(input(">>>"))
        saldoTotal += valor
        extrato.append({
            "Depósito": f'R$ {valor}'
        })
    if operacao == 2:
        if saquesTotal < 3:
        
        
            print("Informe o valor do saque")
            valor = float(input(">>>"))
            if valor > 500:
                print("Saque maior que o limite permitido")
            elif valor > saldoTotal:
                print("Saldo insuficiente")
            else:
                saldoTotal -= valor
                extrato.append({
                "Saque": f'R$ {valor}'
                })
                saquesTotal += 1
        else:
            print("Limite de saques atingidos")
    if operacao == 3:
        for item in extrato:
            print(item)
        print(f'Saldo Total: R$ {saldoTotal}')
    if operacao == 4:
        saida = True



    

