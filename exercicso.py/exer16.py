
palavracomparada = "roma"
anagrama = "rima"
tamanhodepalavra = len(palavracomparada)
tamanhodeanagrama = len(anagrama)

if tamanhodeanagrama == tamanhodepalavra:
       if sorted(anagrama) == sorted(palavracomparada):
            print(f"é um anagrama de {anagrama}")
       else:
            print(f"não é um anagrma de {palavracomparada}")
else:
    print("não é um anagrama")