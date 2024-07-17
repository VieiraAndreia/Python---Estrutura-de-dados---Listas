#Programa que tem as listas A e B com 10 elementos, onde A possui valores divisíveis por 2 e 3 e B possui valores múltiplos de 5. No final apresentar uma lista C com a junção de A e B.

a=[6,12,18,24,30,36]
b=[5,10,15,20,25,30]
c=[]

for i in range(1):      
    c.append(a+b)    

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")