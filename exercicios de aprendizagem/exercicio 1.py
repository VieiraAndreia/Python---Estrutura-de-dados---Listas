#Programa que lê 10 números de uma lista A e cria uma lista B, seguindo a regra: índices com numeros ímpares se soma 5 e numeros pares multiplica-se por 5.

a=[]
b=[]
for i in range (1,6):                                  # "i" representa o total de elementos
    a.append(int(input(f"Digite o {i} número:")))      #números que vão ser adicionados na lista "a"
    if (i-1)%2==0:                                     # o if verifica se o índice é  par  
        b.append(a[i-1]*5)                             # "a[i-1]" é o número que está nesse índice
    else:                                              # o else serve para os índices ímpares
        b.append(a[i-1]+5)
print(a)
print(b)