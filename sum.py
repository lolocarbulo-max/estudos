matriz = [
    [3, 7, 2],
    [8, 1, 4],
    [6, 5, 9]
] 

total = 0# sempre quando precisar somar valores de lista crir uma variavel vazia e depois faz um novo valor para ela com o antigo e
for l in matriz:
    total = total + sum(l)
print(total) 
    
