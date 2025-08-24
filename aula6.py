
def entrada(senha):
    for tentativas in range(3):
        senha=str(input("escreva a senha: "))
        if senha =="senha123":
            print("Bem-vindo")
            exit()
        else:
            print("senha errada")

print("Acesso bloqueado")

print(entrada())