class cachorro():
    def __init__(self,idade,cor):
        self.idade = idade
        self.cor = cor
    def __repr__(self):
        return(f"idade: {self.idade} cor: {self.cor}")
cachorro1 = cachorro(5, "preto")
print(cachorro1)

