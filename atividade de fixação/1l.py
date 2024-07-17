#Programa que lê uma lista A com 10 elementos e  origina uma lista B onde cada elemento de é a metade do elemento de A.

a=[]
b=[]

for i in range(10):    #controla os índices
    a.append(int(input(f"Digite o {i+1}° valor para a lista A:")))   # valores adicionados em A
    b.append(a[i]/2)                                              # valores adicionados em B, de acordo com a regra.
print(b)