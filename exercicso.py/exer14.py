matriz = [[0] * 9 for matrz2 in range(1,10)]

for linhas,colunas in enumerate(matriz):
    for linhas2,colunas2 in enumerate(colunas):
         matriz[linhas][linhas2]  =  linhas2 +1 
def validador_de_linhass(linhas):
     conjunto_linhas = set(matriz[linhas])
     if conjunto_linhas == {1,2,3,4,5,6,7,8,9}:
          return True

def validador_de_colunas (j):
     listadecolunas = set(matriz[ma][j] for ma in range(0,9) )
     if listadecolunas == {1,2,3,4,5,6,7,8,9}:
          return True
     else:
          return False


def validador_de_3 (bi,bj):
     valida=set(matriz[li][lj] for li in range(bi*3,bi*3 +3)for lj in range(bj*3 ,bj*3 +3 ))  
     if valida == {1,2,3,4,5,6,7,8,9}:
          return True
     else:
          return False
def função_mestre ():
     for i in range(0,9):
          if not validador_de_linhass(i):
               return False
     for A in range(0,9):
          if not validador_de_colunas(A):
               return False
             
     for bi in range(0,3):
          for bj in range(0,3):
               if not validador_de_3(bi,bj):
                  return False
            
     return True

