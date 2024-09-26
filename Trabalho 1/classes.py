
class Veiculo:
    def __init__(self, nome, placa, cor, ano, marca, tipo, valor, kmi, status):
        self.tipo = tipo
        self.cor = cor
        self.nome = nome
        self.placa = placa
        self.marca = marca
        self.ano = ano
        self.valor = valor
        self.kmi = kmi
        self.status = status

    def get_placa(self):
        return self.placa
    
    
    



    
        
class Cliente:
    def __init__(self, nome_cliente, cpf, tel, email, cnh, historico):
        self.cnh = cnh
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.historico = historico
    
    def get_nome(self):
        return self.nome_cliente
    
    def get_cpf(self):
        return self.cpf
    
    def get_tel(self):
        return self.tel
    
    def get_email(self):
        return self.email
    
    def get_cnh(self):
        return self.cnh

class Aluguel:
    def __init__(self, datai, dataf, valort, sts_pagamento): 
        self.datai = datai
        self.dataf = dataf
        self.valort = valort
        self.sts_pagamento = sts_pagamento


class SistemaAluguel:
    def __init__(self,) -> None:
        pass

#VALUES ({self.nome}, {self.placa}, {self.cor}, {self.ano}, {self.marca}, {self.tipo}, {self.valor})