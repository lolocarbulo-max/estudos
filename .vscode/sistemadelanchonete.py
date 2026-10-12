class Produto:
    def __init__(self,nome, quantidade,  estoque_minimo):
        self.nome = nome
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        
    def entrada_de_novos_produtos(self,quantia_de_mercadoria):
        if quantia_de_mercadoria > 0 :
          self.quantidade += quantia_de_mercadoria
          return self.quantidade
        else:
              return " entrada invalida por causa da quantidade "
    def vendas(self,quantidade_vendida):
        if self.quantidade >= quantidade_vendida and quantidade_vendida > 0 :
                    
            self.quantidade -= quantidade_vendida
            return self.quantidade        
        else:
            return f"a quantidade {self.quantidade} e volor não batem para a venda "
    def estoque_baixo(self):
         return self.quantidade <= self.estoque_minimo
class Estoque:
     def __init__(self,):
          self.produtos = []
          
     def adicionar_ao_estoque(self,produto):
             self.produtos.append(produto)
             return "cadastro feito "
     def resumo(self):
           for elementos in self.produtos:
                       print(f"produtos = {elementos.nome}, quantidade = {elementos.quantidade}")
     def alerta(self):
           for elementos_dentro_da_lista in self.produtos:
                 if elementos_dentro_da_lista.estoque_baixo():
                       print(elementos_dentro_da_lista.nome)
                       print(elementos_dentro_da_lista.quantidade)
     def buscar(self,nome):
           for produtoos in self.produtos:
                 if produtoos.nome == nome:
                       return produtoos
coxinha1 = Produto("coxinha",12,5)
produtus = Estoque()
refrigerante1 = Produto("refrigerante",4,5)
produtus.adicionar_ao_estoque(coxinha1)
produtus.adicionar_ao_estoque(refrigerante1)
while True:
        print("1 resumo")
        print("=" * 45)
        print("2 alertas")
        print("=" * 45)
        print("3 registrar venda")
        print("=" * 45)
        print("4 entrada de mercadoria")
        print("=" * 45)
        print("5 adicionar produto novo")
        print("=" * 45 )
        print("0 = sair ")
        print("=" * 45 )
        opecao = int(input("digite uma opecação"))

        if opecao == 1 :
              produtus.resumo()
        elif opecao == 2 :
              produtus.alerta()
        elif opecao == 3 :
              pordt = int(input("digite a quantidade"))
              pordt2 = input("digite o nomedo produto ") 
              a = produtus.buscar(pordt2)
              if a == None:
                    print(f"produto {pordt2} não encontrado")
              else:
                    print(a.vendas(pordt))
        elif opecao == 4 :
            pordt = int(input("digite a quantidade"))
            pordt2 = input("digite o nomedo produto ") 
            a = produtus.buscar(pordt2)
            if a == None:
                print(f"produto {pordt2} não encontrado")
            else:
                  print(a.entrada_de_novos_produtos(pordt))
        elif opecao == 5:
              quantidade2 = int(input("digite a quantidade em numeros"))
              nome2 = input("digite o nome do produto")
              estoque_minimo = int(input("difite a quantidade minima que vc quer para o estoque"))
              produto2 = Produto(nome2,quantidade2,estoque_minimo)
              produtus.adicionar_ao_estoque(produto2)
              print("produto adicionada com sucesso")
        elif opecao == 0:
              break
        else:
              print("opcçaõ inixestente ")
     