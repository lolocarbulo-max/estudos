
class comodo :
    def __init__(self,nome):
                self.nome = nome
    def __str__(self):
             return (f"{self.nome}")
class casa:
        def __init__(self,cor,tamanho):
                self.cor = cor
                self.tamanho = tamanho
                self.comodo = comodo("sala")
        def __str__(self):
                return (f"{self.comodo}")
a = casa("vermelha","4x4")
print(a)