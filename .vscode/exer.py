numeros = [1,2,3]
numero_maior = numeros[0]# defin como o primeiro valor maior 
if numeros[1]>numero_maior:#verifico se o primeiro é maior que o segundo  se for fica se não muda
    numero_maior = numeros[1]
if numeros[2]>numero_maior:
    numero_maior = numeros[2]#mesma coisa só com o novo valor pois a comparação primeira de true 
print(numero_maior)