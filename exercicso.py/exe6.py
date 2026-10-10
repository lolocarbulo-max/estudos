palavra = "Ame a ema"
palavar = palavra.lower().replace(" ","")
if  palavar[:: -1] == palavar:# isso [::-1] é só um fatiamento sem começo e fim só de onde anda 
    print("é um palindromo ")
else:
    print("não é um palidromo ")