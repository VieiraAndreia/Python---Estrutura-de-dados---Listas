#Programa que tem uma lista A com 15 elementos e origina uma lista B com as regras: elementos com indices pares se dividem por 2 e impares multiplicam-se por 1.5

a=[]
b=[]

for i in range(2):                                         # controla os índices
    a.append(int(input(f"Digite o {i+1}° valor para a lista A: ")))  # valores adicionados em A
    if i%2==0:
        print(b.append(a[i]/2))            # valores adicionados em B, de acordo com o if 
    else:
        print(b.append(a[i]*1.5))          # valores adicionados em B, de acordo com o else
print(f"Lista A: {a}")
print(f"Lista B: {b}")