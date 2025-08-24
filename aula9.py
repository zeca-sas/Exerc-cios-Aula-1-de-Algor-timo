CPF=input("escreva seu CPF: ",)

def veri_cpf(CPF):
    if len (CPF) == 11:
        if CPF.isdigit():
          return("CPF está correto")
        else:
          return("por favor apenas utilize numeros")
    else:
          return("por favor coloque 11 caractres")

print(veri_cpf(CPF))

