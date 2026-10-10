s = []
with open(r"C:\Users\loloc\OneDrive\Área de Trabalho\codigos\dados.csv", "r") as f:
    f.readline()
    for l in f:
       s.append(l.strip("\n").strip("\r").split(","))

print(s)


    
