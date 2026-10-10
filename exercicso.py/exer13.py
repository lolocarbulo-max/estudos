import random
numero_secreto = random.randint(1,100)
tentativas = 0 

while tentativas < 6:
    numero_tentado = int(input("digite um numero"))
    if numero_tentado == numero_secreto:
        print("vc acertou parabens")
        break
    elif numero_tentado < numero_secreto:
        print("e maior ")
        tentativas += 1
    elif numero_tentado > numero_secreto:
        print("é menor")
        tentativas +=1 
print(f"oce perdeu o numero era : {numero_secreto}")