#Programa que lê uma lista e apresenta os valores

a=[]
for i in range(1, 11):
    a.append(int(input("Digite o número:")))
    
#for j in range (10,0,-1):   #apresentar os resultados de maneira inversa
    #print([j])
    
print(a)
a.reverse()
print(a)