from Cliente import *
class ContaCorrente:
    def __init__ (self, numeroConta, saldo, cliente):
        self.numeroConta = numeroConta
        self.saldo = saldo
        self.cliente = cliente

    def sacar(self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def exibeDados(self):
        return f"{self.cliente.nome} seu CPF é: {self.cliente.cpf}, sua conta é {self.numeroConta} e seu saldo é de R${self.saldo}"