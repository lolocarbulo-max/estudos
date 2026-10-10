class Saldo:
    def __init__(self,saldo,chave):
        self.saldo = saldo
        self.__chave = chave
    def sacar(self,chave):
        if  chave ==  self.__chave:
            self.saldo = self.saldo - 400
            print(f"a soque foi concluido o saldo agora e de {self.Saldo}")
           
chave = Saldo(1500,"ola")

chave.sacar("ola")
