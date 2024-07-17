#Programa com as listas A (elementos somente com numeros pares ) e B (elementos somente com numeros impares) que origina uma lista C (junção das listas A e B)

a=[]
b=[]
c=[]

for i in range(2):     #controla os ìndices 
    n=int(input(f"Digite um numero: "))    #números que vão ser adicionados nas lista A e B
    if n%2==0:                 # if verifica se o número é par 
        a.append(n)            # valores adicionados em A
    else:                         
        b.append(n)            # valores adicionados em B
    
c.append(a+b)             # valores adicionados em C (uso da concatenação )
    
print("Lista A:", a)
print("Lista B:", b)
print("Lista C:", c)