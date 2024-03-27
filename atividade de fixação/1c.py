#Programa que lê duas lista(A,B) com 20 elementos e constroi uma lista C, onde os elementos de C é a subtração dos elementos correspondentes entre A e B

a=[]
b=[]
c=[]

for i in range (21):
    a.append(int(input(f"Digite o {i+1} elemento de numero A:")))
    b.append(int(input(f"Digite o {i+1} elemento de numero B:")))
    c.append((a[i] - b[i]))
    
    print(f"A lista C é: {c}")