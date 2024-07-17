#Programa que lê uma lista A com 10 elementos positivos, cria uma lista B que deverá ter como elemento o valor oposto do elemento de A.

a=[]
b=[]
cont=0
for i in range(5):             #controla a quantidade de elementos
    while  cont<5:             # controla os índices
        valor=int(input(f"Digite o {cont+1}° valor para a lista A:"))  # valores que vão ser adicionados em A
        if valor>0:                                           # o if verifica se os valores são positivos
            a.append(valor)                                   # lista com valores
            b.append(a[cont]*-1)                              # valores adicionados em B, de acordo com a regra
            cont+=1
        else:                                                  #Usado para quando for digitado um valor negativo
            print("Esse valor é inválido!")
print("Lista A:",a)
print("Lista B:",b)