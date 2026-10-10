class Produto:
    def __init__(self,nome, quantidade,  estoque_minimo):
        self.nome = nome
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        
    def entrada_de_novos_produtos(self,quantia_de_mercadoria):
        self.quantidade += quantia_de_mercadoria
        return self.quantidade
    def vendas(self,quantidade_vendida):
        if self.quantidade >= quantidade_vendida:
                    self.quantidade -= quantidade_vendida
                    return self.quantidade        
        else:
            return f"não da para vender mais de o que tem  e vc só tem {self.quantidade}"
    def estoque_baixo(self):
         return self.estoque_minimo<=0
         
coxinha1 = Produto("coxinha",4,5)
print(coxinha1.vendas(20))
print("olamundo ")
