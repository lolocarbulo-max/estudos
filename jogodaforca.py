palavra = ("chocolate")

tentativas = 0 

def verificar_palavra(palavra):  
 while True:
    palavra1 = input("digite uma palavra: ")
    if palavra == palavra1:
        print("parabens vc acertou  a palavra")
        print("voce ganhou")
        break
    elif palavra1 < "a" or palavra1 > "z":
        print("entrada inválida. digite apenas letras do alfabeto.")
    else:
        print("vc errou a palavra")
        print("tente novamente")
while tentativas < 3 :
   tentativas += 1
   verificar_palavra(palavra)