#Ler as listas A com 20 elementos e B com 30 elementos, construir uma lista C que deve ser a junção das listas A e B
a=[]
b=[]
c=[]

for i in range (21):                                         # controla os índices                                 
    a.append(int(input(f"Digite o {i+1}° valor da lista A: ")))    # valores adicionados em A
    b.append(int(input(f"Digite o {i+1}° valor da lista B: ")))    # valores adicionados em B
c.append(a + b)                                                # valores adicionados em C, usando concatenação
print("Lista A:", a)
print("Lista B:", b)   
print("Lista C:", c )   