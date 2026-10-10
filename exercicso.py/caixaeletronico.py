notas_disponiveis = [100,50,20,10,5,2]
valor_final = int(input("digite um numero para ver quantas notas cabem nela "))
quantidade = 0 
for notas in notas_disponiveis:
    valor_atual = valor_final// notas
    valor_final = valor_final % notas
    if valor_atual> 0 :
        print(f"{valor_atual} notas {notas}")