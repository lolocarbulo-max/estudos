senha_a_se_verificda = input("digite uma senha")
vazio = []
tem_digito = None 
if len(senha_a_se_verificda)==8 :
    for senha in senha_a_se_verificda: 
       if senha.isupper() :
          vazio.append(senha)
       if senha.isdigit():
           tem_digito= senha
       else:
           print("precisa ter um numero é um digito")
        
else:
    print("precisa ter 8 caracterise")  
if vazio and tem_digito:
    print(f"sua {senha_a_se_verificda} é forte")
 