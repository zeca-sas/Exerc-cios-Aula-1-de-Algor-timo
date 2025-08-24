N_daluno=int(input("coloque quantos alunos estão na sala: "))
M_notas=[]


for alunos in range(N_daluno):
    nota=int(input("escreva a nota dos alunos: "))
    M_notas.append(nota)


#média
média=sum(M_notas)/N_daluno
print(média)


#maior_menor
M_notas.sort()
print(M_notas[0],M_notas[-1])


#percentual>média
N_altas=[]
for num in M_notas:
    if num > média:
        N_altas.append(num)
Maior_M=len(N_altas)
print(Maior_M)
resultado=(Maior_M*100)/N_daluno
print(resultado)