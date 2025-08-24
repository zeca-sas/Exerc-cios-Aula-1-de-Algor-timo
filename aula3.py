num=int(input("Digite um numero: "))
V_divi=0


for c in range(1, num +1):
   if num % c == 0:
    V_divi +=1
if V_divi == 2:
    print("é primo")
else:
    print("não é primo")

