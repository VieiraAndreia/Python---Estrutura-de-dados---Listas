#Programa que tem uma lista A com 20 elementos, forma uma lista B com elementos correspondentes ao somatório do mesmo elemento de A.

a=[]
b=[]

for i in range (2):
    a.append(int(input("Digite um número para a lista A:")))
#2° loop
    somatorio=0
    for j in range (a[i]+1):
        somatorio+=j
    b.append(somatorio)
print(f"Lista A: {a}")
print(f"Lista B: {b}")