palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'mercado')
for a in palavras:
    print(f"Na palavra {a.upper()} temos: ", end="")
    for aa in a:
        if aa in "aeiou":
            print(aa, end="")
print()