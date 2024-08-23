extrato = []
saldoTotal = 0
saida = False
transacoesTotal = 0
from datetime import datetime


while (saida == False):
    print("Escolha uma operação")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    operacao = int(input(">>>"))
    if operacao == 1:
        if transacoesTotal < 10:
            print("Informe o valor do deposito")
            valor = float(input(">>>"))
            saldoTotal += valor
            extrato.append({
                "Hora": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                "Operação": "Depósito",
                "valor": f'R$ {valor}'
            })
            transacoesTotal += 1
        else: 
            print("Limite de transações atingido")
    if operacao == 2:
        if transacoesTotal < 10:
        
        
            print("Informe o valor do saque")
            valor = float(input(">>>"))
            if valor > 500:
                print("Saque maior que o limite permitido")
            elif valor > saldoTotal:
                print("Saldo insuficiente")
            else:
                saldoTotal -= valor
                extrato.append({
                "Hora": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                "Operação": "Saque",
                "Valor": f'R$ {valor}'
                })
                transacoesTotal += 1
        else:
            print("Limite de transações atingidos")
    if operacao == 3:
        for item in extrato:
            print(item)
        print(f'Saldo Total: R$ {saldoTotal}')
    if operacao == 4:
        saida = True



    

