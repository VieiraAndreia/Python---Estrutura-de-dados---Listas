#Ler 15 elementos de uma Lista A e construir uma lista B, sendo que os elementos de B são o quadrado dos elementos de A

a=[]
b=[]

for i in range(0,15):                     # "i" é a quantidade de índices
    a.append(int(input(f"Digite o {i+1}° elemento da lista A:"))) # valores adicionados em A
    b.append(a[i]**2)                     # valores adicionados em B de acordo com a regra
    print(f"A lista B é: {b}")