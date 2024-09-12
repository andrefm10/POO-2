class Carros:
    def __init__(self, nome, cor, tipo, local, qualidades):
        self.tipo = tipo
        self.nome = nome
        self.cor = cor
        self.local = local
        self.qualidades = qualidades
    
    def aluga_carro(self):
        print("")