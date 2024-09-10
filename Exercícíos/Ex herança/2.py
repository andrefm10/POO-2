class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    def get_valor(self):
        return self.valor
    
class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valorvip = (valor+25)
    def get_valorvip(self):
        return self.valorvip

class CamaroteSuperior(VIP):
    def __init__(self, valor, loc):
        super().__init__(valor)
        self.valorcam = (valor+50)
        self.loc = loc
    def get_loc(self):
        return self.loc
    def get_valorcam(self):
        return self.valorcam

valor = 70
ing = Ingresso(valor)
vip = VIP(valor)
#listaing = []

op = int(input("Qual ingresso você quer comprar? \n1- Normal\n2-VIP\n3-Camarote\n"))

if op == 1:
    print(f"Você comprou o ingresso com sucesso, custando R$ {ing.get_valor()}")

if op == 2:
   print(f"Você comprou o ingresso com sucesso, custando R$ {vip.get_valorvip()}")

if op == 3:
    loc = input("Qual a localização desejada: ")
    cam = CamaroteSuperior(valor,loc)
    print(f"Você comprou o ingresso com sucesso, custando R$ {cam.get_valorcam()} e no(a) {cam.get_loc()}")

