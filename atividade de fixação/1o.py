#Programa que tem uma lista A de 25 elementos com temperaturas em graus Celsius e criará uma lista B com os elementos de A convertidos para Fahrenheit.

a=[]
b=[]

for i in range(5):                                                 # controla os índices
    a.append(int(input(f"Digite o {i+1}° valor para a temperatura em °C: ")))   # valores adicionados em A
    conv=(9*a[i]+160)/5                                            # calculo para a conversão de °C em °F
    b.append(conv)                                                 # valores da "conv" adicionados em B

print(f"Lista A (°C): {a}")
print(f"Lista B (°F): {b}")