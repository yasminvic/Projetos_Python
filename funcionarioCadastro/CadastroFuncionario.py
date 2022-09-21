from funcionario import *

lista = []
soma = 0

while True:
    nome = input("Digite seu nome: ")
    if nome.casefold() == "fim".casefold():
        break
    salario = float(input("Digite seu salario: "))
    codigoCargo = int(input("Digite seu código de cargo: "))

    funcionario = Funcionario(nome, salario, codigoCargo)
    lista.append(funcionario)

for funcionario in lista:
    soma += funcionario.salario

print(f"A soma de todos os salários antes do aumento é de R${soma}")

for funcionario in lista:
    if funcionario.codigoCargo == 1:
        funcionario.aumentarSalario(5)

    elif funcionario.codigoCargo == 2:
        funcionario.aumentarSalario(10)

    else:
        funcionario.aumentarSalario(8)

soma = 0
for funcionario in lista:
    soma += funcionario.salario

print(f"A soma de todos os salários depois do aumento é de R${soma}")