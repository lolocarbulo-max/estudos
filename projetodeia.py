

while True:
         
        pergunta = input(" o que vc quer conversar , digite sair para sair")
        if "python" in pergunta  :
                print(" python é um linguagens muito versitia onde suas funções são bem facieas de aprender  ") 
        elif "matematica" in pergunta :
              print("a matematica e uma materia essencial ")
        elif "sair" in pergunta or  " falo " in pergunta or  "vou vazar" in pergunta : #  or compara operações para verse são verdadeiras ou falsaas  então sempre colocar uma operação  quando quero que o ocnnputador  tenha  perguntas de alternamcia 
             print("ok falo ") 
             break
        else:
             print(" não entendi sua pergunta ") 

    