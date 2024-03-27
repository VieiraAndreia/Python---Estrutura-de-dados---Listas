#Programa que lê cindo numeros inteiros de uma lista A e apresenta a soma dos elementos da lista que sejam ímpares.

a=[]
soma=0
for i in range (0,5):
     a.append(int(input("Digite o número:")))
     if a[i]%2!=0:
         soma+=a[i]
print("A soma dos numeros impares é:", soma)