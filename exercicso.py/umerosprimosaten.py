n = int(input("diigte um numero"))
lista = [0 for x in range(0,n+1)]
for numeros in range(2,n+1):
    for numero_para_riscar in range(numeros *2,n+1,numeros):
        lista[numero_para_riscar] = 1 
for numeros_para_exibiir in range(2,n+1):
    if lista[numeros_para_exibiir] == 0:
      print(lista[numeros_para_exibiir])