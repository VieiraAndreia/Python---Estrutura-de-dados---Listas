#Programa que lê as listas A, B e C com 5 elementos e constrói uma lista D juntando as listas A, B e C.

a=[]
b=[]
c=[]
d=[]

for i in range (1):                                                  # controla os índices
    a.append(int(input(f"Digite o {i+1}° valor da lista A:  ")))     # valores adicionados em A
    b.append(int(input(f"Digite o {i+1}° valor da lista B:  ")))     # valores adicionados em B
    c.append(int(input(f"Digite o {i+1}° valor da lista C:  ")))     # valores adicionados em C
    d.append(a + b + c)                                              # valores adicionados em D, usando concatenação
print("Lista A:", a)
print("Lista B:", b)   
print("Lista C:", c )   
print("Lista D:", d)