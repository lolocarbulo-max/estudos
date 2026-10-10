estoque = {
    "eletronicos": {"tv": 5, "notebook": 2},
    "roupas": {"camisa": 10, "calca": 7}
}
menor = None#pode ser tamem vazio 
for a,b in estoque.items():
    for c,d in b.items():
     if menor is None:
        menor = (c,d) 
    else:
        if d < menor[1]:
           menor = (c,d)
print(menor) 