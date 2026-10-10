matriz = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]
conta  = 0 
total_dde_linhas =  []
for linhas, elementos in enumerate(matriz):
    conta = sum(elementos)
    total_dde_linhas.append(conta)
print(total_dde_linhas)
print(max(total_dde_linhas))
print(total_dde_linhas.index(max(total_dde_linhas)))