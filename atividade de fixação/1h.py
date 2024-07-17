#Programa com uma lista A de 20 elementos, cria a uma lista B com os mesmos elementos de maneira inversa.

a =[]
b =[]

for i in range(2):                                              #controla os índices
    a.append(int(input(f"Digite o {i+1}° valor da lista A: ")))  # valores adicionados em A
print(f"Lista A: {a}")
a.reverse()                                                  # comando para revertar a lista A
b.append(a)                                                  # valores adicionados em B
print(f"Lista B: {b}")

#forma feita em sala: 
#lista=[]
#for i in range (10):
    #lista.append(int(input("Digite um número para a lista A:")))
#print(lista)  
#for i in range(9,-1,-1):  #For para inverter os números , o -1 como incremento é o ultimo elemento.
    #print(lista[i])