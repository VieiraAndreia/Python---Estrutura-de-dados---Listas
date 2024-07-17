#Programa que lê uma lista A de 15 elementos e apresenta o total de elementos pares existentes na lista.

a=[]
par=0

for i in range(2):        #controla os índices
    num=int(input(f"Digite o {i+1}° valor da lista A: "))    #números que vão ser adicionados na lista A 
    a.append(num)     # valores adicionados em A
    if a[i]%2==0:     # o if verifica se o elemento de a[i] é par 
        par+=1        # acumula a quantidade de valores pares
print(f"Lista A: {a}")
print(f"A quantidade de elementos pares é: {par}")