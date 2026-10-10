#fibonacci
sequencia = int(input("digite um numero para fazer a sequencia "))
ponteira1 =  0
ponteira2 = 1
print(ponteira1) 
print(ponteira2)
for termos in range(sequencia -2):
    terceiro_ttermo = ponteira1 + ponteira2
    ponteira1 = ponteira2
    ponteira2 = terceiro_ttermo
    print(terceiro_ttermo)
    
   
