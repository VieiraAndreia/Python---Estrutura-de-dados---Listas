#Programa que lê duas listas A e B  com 15 elementos e constrói uma lista C, onde  C deve ter  30 elementos (A+B).

a=[]
b=[]
c=[]

for i in range (15):                                               # controla a quantidade de índices
    a.append(int(input(f"Digite o {i+1}° elemento da lista A:")))  # valores adicionados em A
    b.append(int(input(f"Digite o {i+1}° elemento da lista B:")))  # valores adicionados em B
    soma=(a[i] + b[i])*2                                # "soma" calcula os valores da lista C usando a concatenação
    c.append((soma))
    
print(f"A lista C é: {c}")

#OBS:
#concatenação: junção(+) de duas ou mais variáveis/strings