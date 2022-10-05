class Turma:
    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao
        self.alunos = []

    def addAluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            return f"Aluno: {aluno.matricula}, {aluno.nome} foi matriculado na turma {self.codigo}, {self.descricao}"
        else:
            return f"Aluno: {aluno.matricula}, {aluno.nome} já está matriculado na turma {self.codigo}, {self.descricao}"

    def delAluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            return f"Aluno: {aluno.matricula}, {aluno.nome} removido da turma {self.codigo}, {self.descricao}"
        else:
            return f"Aluno: {aluno.matricula}, {aluno.nome} não está matriculado na turma{self.codigo}, {self.descricao}"