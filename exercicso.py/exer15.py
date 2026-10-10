palavra_quevaiserverificada = "A mala nada na lama"
palava = palavra_quevaiserverificada.lower().replace(" ","")
if palava[::-1] == palava:
    print("é um palindromo")
else:
    print("não é um palindromo ")