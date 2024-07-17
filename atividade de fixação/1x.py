# Programa que lê uma lista A de 6 elementos e constrói uma lista B, onde os elementos dos índices ímpares de B devem ser os elementos dos índices pares de A e os elementos de índice par de B devem ser os elementos de índice ímpar de A.

a=[]
b=[]

for i in range(6):
    num=int(input(f"Digite o {i+1}° valor da lista A: "))  #números que vão ser adicionados na lista A
    a.append(num)
    
    if i%2==0:
        b.append(a[i])
    else: 
        b.append(a[i])
print(f"Lista A: {a}")
print(f"Lista B: {b}")