#Programa que lê uma lista A com 15 elementos e constrói uma lista B onde cada elemento de B é o fatorial de um elemento de A 

a=[]
b=[]

for i in range (16):                    #controla os primeiros elementos
    a.append(int(input(f"Digite o {i+1}° valor da lista A:")))   # valores adicionados em A
    #2° loop
    fatorial=1
    for j in range (1,a[i]+1):  # controla os valores de j para calcular o fatorial
        fatorial*=j             # multiplica o valor de j atual com o valor atual de fatorial
        b.append(fatorial)      # valores adicionados em B, de acordo com o fatorial calculado
print(f" Lista A: {a}")        
print(f" Lista B: {b}")