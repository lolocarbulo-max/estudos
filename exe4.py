class funcionario:
    def __init__(self,nome,salario):
        self.salario = salario
        self.nome = nome
    def descriça(self):
        print(f"ola o meu nome é {self.nome} e meu salario é {self.salario}")
class gerente(funcionario):
    def __init__(self, nome, salario,equipe):
        super().__init__(nome,salario)
        self.equipe = equipe   
    def descriça(self):
        print(f"oi meu nome é {self.nome} o meu salario é {self.salario} e minha equipe é {self.equipe} e tomanho dela é de {len(self.equipe)}")
funct = funcionario("lucas",12345)            
objto = gerente("lucas",1000,["lucas","mario","rogerio"])
objeto1 = [objto,funct]
for a in objeto1:
  a.descriça()