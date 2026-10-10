class conta:
    juros = 0.2
    def __init__(self,saldo):
        self.saldo = saldo
    def juro (self):
       self.saldo = self.saldo + (self.juros * self.saldo)
       return self.saldo
       
saldo_b = conta(1500)
saldo_a = conta(12345678)
print(saldo_a.juro())
print(saldo_a.saldo)
