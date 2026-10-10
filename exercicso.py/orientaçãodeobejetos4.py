class Livro:
    contador = 0 
    def __init__(self,titulo,autor,data_de_lançamento,):
        self.titulo = titulo
        self.autor = autor
        self.data_de_lançamento = data_de_lançamento
        self.estado = False
        Livro.contador +=1 
    def status(self):
        self.estado = True  
        
    def retornar_status(self):
        return self.estado
    def __repr__(self):
      return (f"nome = Livro , titulo = {self.titulo!r}, estado de empréstimo = {self.estado}")  
    def mudarestado(self):
        self.estado = False
    def __str__(self):
        return (f"o livro {self.titulo} , do autor {self.autor} do ano {self.data_de_lançamento}")
class Biblioteca:
     
     def __init__(self):
         
         self.listas_de_livross = []  
     def emprestar(self,livro):
        if livro not in  self.listas_de_livross:
         return False
        if livro.retornar_status() ==True:
             return False
        livro.status()
        return True 
     def adicionar(self,livros):
         self.listas_de_livross.append(livros)  
     def devolver(self,livro):
        if livro not in  self.listas_de_livross:
            return False
        if livro.retornar_status() == False:
           return False
        livro.mudarestado()
        return True
     def total_de_empréstimos(self):
          emprestados = 0 
          for livro in self.listas_de_livross:
              if livro.retornar_status():
                emprestados += 1
          return emprestados
     def __repr__(self):
          return (f"total de livros = {len(self.listas_de_livross)} ,total de emprestimos = {self.total_de_empréstimos()} ")
     def __str__(self):
         return(f" nome = biblioteca,total de livros é de {len(self.listas_de_livross)}")            
livro1 =Livro("titulo","nom","12/32/45") 
biblioteca1 = Biblioteca()
biblioteca1.adicionar(livro1)
print(repr(biblioteca1))
print(repr(livro1))
print(biblioteca1.emprestar(livro1))
print(repr(biblioteca1))
print(repr(livro1))
print(biblioteca1.devolver(livro1))   # espero: ?
print(biblioteca1.devolver(livro1))   # espero: ?
print(biblioteca1.devolver(Livro("x", "y", "z")))   # espero: ?
print(repr(biblioteca1))
print(repr(livro1))
print(Livro.contador)