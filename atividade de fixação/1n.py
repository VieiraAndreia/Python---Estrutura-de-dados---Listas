#Programa que lê 20 temperaturas °C na lista A e deverá apresentar a menor, a maior e a média das temperaturas lidas.

a=[]
min=0
max=0
soma=0
for i in range (20):                #controla os índices
    temp=float(input(f"Digite o {i+1}° valor de temperatura (°C): "))  #números que vão ser adicionados na lista A 
    a.append(temp)     # valores adicionados em A
    a.sort()           # usado para ordenar a lista em ordem crescente (do menor para o maior)
    soma+=temp         # soma todos os valores da lista
    media=soma/2       # calcula a média das temperaturas
print(f"Lista A: {a}")
print(f"{a[19]}°C é maior temperatura da lista.")
print(f"{a[0]}°C é menor temperatura da lista.")
print(f"A média das temperaturas é: {media}")