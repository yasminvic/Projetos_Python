from Cliente import *
from contaCorrente import *

maior = -1
menor = 9999999999999999999999999999999
contaLista = []

while True:
    nmrconta = input("Digite o número da conta: ")
    if nmrconta == "0":
        break
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    saldo = float(input("Digite o saldo da conta: "))
    
    cliente = Cliente(nome, cpf)
    cnt = ContaCorrente(nmrconta, saldo, cliente)

    contaLista.append(cnt)


if len(contaLista) > 0:
    while True:
        nmrconta = input("Digite o número da conta que deseja pesquisar: ")
        if nmrconta == "0":
            break

        encontrou = False
        for i in contaLista:
            if int(i.numeroConta) == int(nmrconta):
                encontrou = True
                i.exibeDados()
                acao = int(input("Digite 1-Sacar e 2-Depositar: "))
                if acao == 1:
                    valor = float(input("Quanto você deseja sacar: "))
                    if i.sacar(valor) == True:
                        print("Saque feito com sucesso !!")
                    else:
                        print(f"Saque da conta {i.numeroConta} não realizado")
                    break
                elif acao == 2:
                    valor = float(input("Quanto você deseja depositar: "))
                    if i.depositar(valor) == True:
                        print("Deposito feito com sucesso !!")
                    else:
                        print(f"Deposito da conta {i.numeroConta} não realizado")
                    break
                else:
                    print("!COMANDO INVÁLIDO!")
        
        if encontrou == False:
            print("Essa conta não existe!")
            
maior = -1
menor = 9999999999999999999999999999999
for i in contaLista:
    print(i.saldo)
    if maior < i.saldo:
        maior = i.saldo
    if menor > i.saldo:
        menor = i.saldo

for i in contaLista:
    if i.saldo == maior:
        print(f"Maior saldo\n {i.exibeDados()}")
    if i.saldo == menor:
        print(f"Menor saldo\n {i.exibeDados()}")