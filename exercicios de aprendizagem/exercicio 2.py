#Programa que lê cinco numeros inteiros de uma lista A e apresenta a soma dos elementos da lista que sejam ímpares.

a=[]
soma=0                                              
for i in range (0,5):                            # "i" representará os índices 
     a.append(int(input("Digite o número:")))    # elementos que vão ser adicionados a lista 
     if a[i]%2!=0:                               # if verificará se os elementos dos índices serão ímpares
         soma+=a[i]                              # todo valor que atender ao if vai ser atribuído a variável "soma"
print(f"A soma dos números ímpares é: {soma}")