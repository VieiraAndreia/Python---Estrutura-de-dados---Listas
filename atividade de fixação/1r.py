#Programa que lê uma lista A e B com 6 elementos e origina as listas : C - com os elementos de índice impar e D -  com os elementos de indice par.

a=[]
b=[]
c=[]
d=[]

for i in range(2):                                               # controla os índices
    a.append(int(input(f"Digite o {i+1} elemento da lista A:")))   # valores adicionados em A
    b.append(int(input(f"Digite o {i+1} elemento da lista B:")))   # valores adicionados em B
    if i%2!=0:
        print(c.append(a+b))                                      # valores adicionados em C de acordo com a regra
    else:
        print(d.append(a+b))                                        # valores adicionados em D de acordo com a regra
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")
print(f"Lista D: {d}")