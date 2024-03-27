#Programa que lê 10 números de uma lista A e cria uma lista B, seguindo a regra: indices com numeros impares se soma 5 e numeros pares multiplica-se por 5.

a=[]
b=[]
for i in range (1,6):
    a.append(int(input(f"Digite o {i} número:"))) #f é uma formatação que permite usar uma variavel dentro do print.
    if (i-1)%2==0:
        b.append(a[i-1]*5)
    else:
        b.append(a[i-1]+5)
print(a)
print(b)