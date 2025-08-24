Nomes=["zeca","pedro","eduardo","joão","tiago","iaro","antonio"]
nome=str(input("escolha um nome: ")).lower()

def pose(nome):
    if nome in Nomes:
        posicao=Nomes.index(nome)
        return(f"seu nome é o {posicao} na lista")
    else:
        return("esse nome não está na lista")

print(pose(nome))