import sqlite3

class Veiculo:
    def __init__(self, nome, placa, cor, ano, marca, tipo, valor, status):
        self.tipo = tipo
        self.cor = cor
        self.nome = nome
        self.placa = placa
        self.marca = marca
        self.ano = ano
        self.valor = valor
        self.status = status
    
    def cadastro(self):
        cx = sqlite3.connect('aluguel.db')
        cr = cx.cursor()
        
        cr.execute(f'''
            INSERT INTO carros (nome, placa, cor, ano, marca, tipo, valor)
            VALUES ({self.nome}, {self.placa}, {self.cor}, {self.ano}, {self.marca}, {self.tipo}, {self.valor})
        ''')
        cx.commit()
        cx.close()
        print("Cadastro realizado com sucesso!")
        
class Cliente:
    def __init__(self, nome_cliente, cpf, tel, email, cnh, historico):
        self.cnh = cnh
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.historico = historico

class Aluguel:
    def __init__(self, datai, dataf, kmi, valort, sts_pagamento): 
        self.datai = datai
        self.dataf = dataf
        self.kmi = kmi
        self.valort = valort
        self.sts_pagamento = sts_pagamento


class SistemaAluguel:
    def __init__(self,) -> None:
        pass