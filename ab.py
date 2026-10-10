from abc import ABC , abstractmethod
class veiculo(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def mover():
        pass
class hb20(veiculo):
    def __init__(self):
        self.mover = "movendo"
    def mover(self):
        print(self.mover)
v = hb20()

    




