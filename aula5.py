

senha=str(input("escreva a senha: "))
print("senha errada")


for tentativas in range(2):
    senha=str(input("escreva a senha: "))
    if senha =="senha123":
        print("acessou autorizado")
        break
    elif tentativas==0:
        print("acesso negado")
    else:
        print("senha errada")
