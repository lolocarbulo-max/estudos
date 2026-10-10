listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00)

for pos  in range(0, len( listagem), 2 ):  # me ensina sobre como o {f } não só mexe com variaveis 
    print(f"{listagem[pos]:.<30}{listagem[pos + 1 ]:>7.2f}")