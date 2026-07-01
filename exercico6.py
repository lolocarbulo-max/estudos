numero_1 = float(input("digite um numero por favor "))
numero_2 = float(input("digite outro numero por favor "))
def maior_numero(numero_1,numero_2):
    if numero_1 > numero_2 :
        print(f"o numero {numero_1}é maior que o {numero_2}")
    elif numero_2 > numero_1:
        print(f"o numero {numero_2} é maior que o {numero_1}")
    else:
        print(f"os dois nmeros o {numero_1}e o {numero_2} são iguais")
maior_numero(numero_1,numero_2)