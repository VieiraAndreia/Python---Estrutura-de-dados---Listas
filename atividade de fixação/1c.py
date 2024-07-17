#Programa que lê duas listas(A,B) com 20 elementos e constrói uma lista C, onde os elementos de C é a subtração dos elementos correspondentes entre A e B

a=[]
b=[]
c=[]

for i in range (21):               # "i" quantidade de elementos em cada lista
    a.append(int(input(f"Digite o {i+1}° elemento da lista A:")))    # valores adicionados em A
    b.append(int(input(f"Digite o {i+1}° elemento da lista  B:")))   # valores adicionados em B
    c.append((a[i] - b[i]))   # valores adicionados em C, seguindo a regra  
print(f"A lista C é: {c}")