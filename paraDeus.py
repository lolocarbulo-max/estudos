nome = input("digite um nome: ").strip()#strip  serve paraa remover os espaços da estring caso o usuario digite algo com umespaço que não é necesario mas dentro do codigo

def saudacao(nome):
    if nome == "jesus":
        print("jesus é o caminho a verdade e a vida")
    elif nome == "quero saber mais de jesus":
        print("jesus é filho de Deus e Deus enviou seu único filho para nos salvar e para que os que nele creem não pereçam mas tenham a vida eterna")
    else:
        print(f"olá {nome}, seja bem vindo!")

saudacao(nome)