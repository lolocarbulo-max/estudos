palavra = " eu gosto de python"
vogais = "aeiou"
palavra2 = palavra.lower().replace(" ","")# retiro os espaços e transfor um minusculo
total = sum([1 for letras in palavra2 if letras in vogais]) # uma lista comrimida com sum que soma os valores dessa lista com essa condeção
print(f"a palavra tem {total} vogais")