#Programa que lê uma lista de 10 elementos e apresenta os valores

a=[]
for i in range(1, 11):                               # "i" será a quantidade de elementos da lista
    a.append(int(input("Digite o número:")))         # adiciona os elementos a lista
    
print(a)
a.reverse()                                           # "reverse" apresenta os elementos em ordem inversa
print(a)

# OBS: caso não queira usar o "a.reverse": 
#for j in range (10,0,-1):  #apresentar os resultados de maneira inversa
    #print([j])