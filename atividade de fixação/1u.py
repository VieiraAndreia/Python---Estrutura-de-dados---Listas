#Programa que tem as listas A e B com 12 elementos, onde A possui elementos divisíveis por 2 ou 3 e B possui elementos que não sejam múltiplos de 5. No final apresentar a lista C com a junção de A e B.

a=[2,3,4,6,10,9]
b=[12,18,28,36,32]
c=[]

for i in range(1):
    c.append(a+b)
    
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")