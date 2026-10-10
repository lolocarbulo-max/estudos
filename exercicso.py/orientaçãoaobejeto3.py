from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
class Circulo(FormaGeometrica):
    def __init__(self,raio):
        self.raio = raio
    def area(self):
        return self.raio**2 * 3.14
class tringulo(FormaGeometrica):
    def __init__(self, base,altura):
        
        self.altura = altura
        self.base = base
    def area(self):
     return self.base *self.altura / 2  
formageometrica1 = Circulo(34)
formageometrica2 = tringulo(32,12)
print(formageometrica1.area())
print(formageometrica2.area())