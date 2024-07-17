# Programa lê uma lista A com 30 elementos deve apresentar a quantidade de elementos pares e ímpares nessa lista.

a=[]
par=0
impar=0
for i in range(3):            # controla os índices
    num=int(input(f"Digite o {i+1}° valor da lista A: "))  #números que vão ser adicionados nas listas A e B
    a.append(num)            # valores adicionados em A
    if a[i]%2==0:            # o if verifica se o elemento de a[i] é par 
        par+=1               # acumula a quantidade de valores pares
    else:
        impar+=1             # acumula a quantidade de valores ímpares
print(f"Lista A: {a}")
print(f"A quantidade de elementos pares é: {par}")
print(f"A quantidade de elementos ímpares é: {impar}")