#Programa que lê duas listas A e B com 10 elementos cada, constrói uma lista C formada com o quadrado da soma dos elementos de A e B.

a=[]
b=[]
c=[]

for i in range (5):
    num=int(input(f"Digite o {i+1}° valor da lista A: "))  #números que vão ser adicionados na lista A
    num1=int(input(f"Digite o {i+1}° valor da lista B: "))  #números que vão ser adicionados na lista B
    a.append(num)                      # valores adicionados em A
    b.append(num1)                     # valores adicionados em B
    c.append((a[i]+b[i])**2)           # valores adicionados em C de acordo com a regra
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")
