class funcionario:
    def __init__(self,nome,salario):
         self.nome = nome
         self.salario =salario
    def clacular_salario(self):
        return self.salario 
class gerente(funcionario):
    def __init__(self, nome, salario, comissão,):
        super().__init__(nome, salario)
        self.comissão = comissão
    def clacular_salario(self):
        return self.salario + self.comissão
class vendedor(funcionario):
    def __init__(self, nome, salario,amais_pelas_vendas):
        super().__init__(nome, salario)
        self.amais_pelas_vendas = amais_pelas_vendas
    def clacular_salario(self):
        return self.salario + self.amais_pelas_vendas
funcionario1 = gerente("lorenzo",1200,123)
funcionario2 = vendedor("carlo",1345,200)
funciona = [funcionario1,funcionario2]
for f in funciona:
    print(f.clacular_salario())