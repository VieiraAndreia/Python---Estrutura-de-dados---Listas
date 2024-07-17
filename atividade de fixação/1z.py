#Programa que lê uma lista A com 10 elementos e apresenta o total de elementos ímpares da lista e o percentual do valor total de números ímpares em relação a quantidade de elementos da lista

a=[]
impar=0

for i in range(5):
    num=int(input(f"Digite o {i+1}° valor da lista A: "))    #números que vão ser adicionados na lista A 
    a.append(num)     # valores adicionados em A
    if a[i]%2!=0:     # o if verifica se os elementos são ímpares
        impar+=1      # acumula a quantidade de valores pares
    pc=(impar/5)*100  # calcula a porcentagem
print(f"Lista A: {a}")
print(f"A quantidade de elementos pares é: {impar}")
print(f"O percentual de números ímpares é: {pc}%")