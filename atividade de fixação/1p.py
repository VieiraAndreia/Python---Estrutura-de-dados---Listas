#Programa que tem uma lista A com 12 elementos e origina uma lista B com as regras: elementos ímpares multiplacam-se por 2 e os pares se mantem constante

a=[]
b=[]

for i in range(2):               # controla os índices
    a.append(int(input(f"Digite o {i+1}° valor para a lista A: ")))   # valores adicionados em A
    if a[i]%2!=0:                 # verifica se o elemento de A é ímpar
        print(b.append(a[i]*2))   # adiciona em B caso o if seja verdadeira
    else:
        print(b.append(a[i]))     # adiciona em B caso o if seja falso                                        
print(f"Lista A: {a}")
print(f"Lista B: {b}")