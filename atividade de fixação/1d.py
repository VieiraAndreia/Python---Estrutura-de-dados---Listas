#Ler 15 elementos de uma Lista A e construir uma matriz B, sendo que os elementos de B são o quadrado dos elementos de A

a=[]
b=[]

for i in range(0,15):
    a.append(int(input(f"Digite o {i+1} elemento de numero A:")))
    b.append(a[i]**2)
    print(f"O vetor B é: {b}")