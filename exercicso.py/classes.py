class chacoro:
    
    def  __init__(self,nome,idade,cor):
        self._nome = nome
        self.idade = idade
        self.cor = cor
    @property# property faz o seguinte 
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome_novo):
        self._nome = nome_novo
        return nome_novo
rex = chacoro("gerando",12,"amarelo")
print(rex.nome)
rex.nome = "bidu"
print(rex.nome)