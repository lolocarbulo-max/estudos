
matriz = [[0] * 4 for _ in range(4)]
for linhas in range(4):
    for colunas in range(4):
        matriz[linhas][colunas] = linhas * colunas
for linhas in range(4):
    print(matriz)
    