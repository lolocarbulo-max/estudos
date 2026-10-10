lista =   [10, 5, 20, 15]
maior_VALOR =  None
segundo_maior_valor = None#definir valor como nonee quado quero deixar ele sem  nada  
for numeros in lista:
    if maior_VALOR is None or  numeros > maior_VALOR:
        segundo_maior_valor = maior_VALOR
        maior_VALOR = numeros
        
    elif segundo_maior_valor is None or segundo_maior_valor < numeros:
        segundo_maior_valor = numeros
        
print(maior_VALOR)
print(segundo_maior_valor)