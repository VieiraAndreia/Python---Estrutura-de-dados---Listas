#Programa que calcula a tabuada e armazena seu resultado numa lista A.

a=[]
print("Esse programa calcula a tabuada: ")
for i in range (10):                     # controla os índices
    n=int(input("Digite um número:"))    
    e=int(input("Digite a tabuada:"))
    mult=n*e                            # realiza o cálculo da multiplicação
    a.append(mult)                      # valores da "mult" adicionados em A
    
print(f"{n} x {e} = {a}")