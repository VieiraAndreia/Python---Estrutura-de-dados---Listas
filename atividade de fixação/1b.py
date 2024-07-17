#Programa que lê 8 elementos de uma lista A, constrói uma lista B com os elementos de A*3.
a=[]
b=[]

for i in range(0,8):                       # "i" será a quantidade de elementos
    a.append(int(input(f"Digite o {i+1}° elemento da lista A:")))     # valores adicionados em A
    b.append(a[i]*3)                       # regra que estabelece os valores de B
print(f"A lista B é: {b}")