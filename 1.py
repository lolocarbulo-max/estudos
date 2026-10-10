class lampada():
    def __init__(self,cor,voltagem,luminosidade):
        self.cor = cor
        self.luminosidade = luminosidade
        self.voltagem = voltagem
    def ligar(self):
        print("ligado")
    def desligar(self):
        print("desligada")
    def status(self):
        print(f"a cor é {self.cor}a luminosidade é {self.luminosidade}e a voltagem é de {self.voltagem}")
lampada1 = lampada("vermelha",200,123456)
if lampada1.ligar() == "ligado":
    print("A lâmpada está ligada.")
else:
    lampada1.desligar()