#Programa que lê duas listas A e B  com 15 elementos e constroi uma lista C, onde os elementos de C são o dobro dos 30 elementos (A+B).

a=[]
b=[]
c=[]

for i in range (15):
    a.append(int(input(f"Digite o {i+1} elemento de numero A:")))
    b.append(int(input(f"Digite o {i+1} elemento de numero B:")))
    soma=a[i] + b[i]
    c.append((soma*2))
    
    print(f"A lista C é: {c}")