#Programa que lê 8 elementos de uma lista, controi uma lista b com os elementos de a*3.
a=[]
b=[]

for i in range(0,10):
    a.append(int(input(f"Digite o {i+1} elemento de numero A:")))
    b.append(a[i]*3)
    print(f"O vetor B é: {b}")