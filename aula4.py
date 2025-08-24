alunos=int(input("escolha quantos alunos irá querer para ver a média: "))
aluno=alunos
notas=0

while alunos != 0:
    nota=float(input("de a nota dos alunos: "))
    notas=notas+nota
    print(notas)
    alunos= alunos -1

notas=notas/aluno
print(notas)