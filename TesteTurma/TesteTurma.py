from Turma import *
from Aluno import *

programacaoI = Turma("POO", "Programacao I")
historia = Turma("HIS", "História")
engenhariaSoft = Turma("ENG", "Engenharia de Software")

joao = Aluno('001', 'João da Silva')
maria = Aluno('002', 'Maria dos Santos')
henrique = Aluno('003', 'Henrique Mattos')
pedro = Aluno('004', 'Pedro Gonçalves')
felipe = Aluno('004', 'Felipe Martins')

print(programacaoI.addAluno(joao))
print(programacaoI.addAluno(maria))
print(programacaoI.addAluno(henrique))
print(programacaoI.addAluno(henrique))
print(programacaoI.delAluno(joao))
print(programacaoI.delAluno(felipe))
print(historia.addAluno(joao))
print(historia.delAluno(henrique))
print(historia.addAluno(felipe))
print(engenhariaSoft.delAluno(felipe))