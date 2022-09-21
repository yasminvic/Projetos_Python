class Funcionario:
    def __init__ (self, nome, salario, codigoCargo):
        self.nome = nome
        self.salario = salario
        self.codigoCargo = codigoCargo

    def aumentarSalario(self, porcentagem):
        porcentagem = porcentagem/100
        self.salario += porcentagem * self.salario

