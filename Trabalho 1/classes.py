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

    def __str__(self):
        return f"{self.marca} {self.nome} -- Placa: {self.placa}, Cor: {self.cor}, Ano: {self.ano}, Categoria: {self.tipo}, Valor por dia: R$ {self.valor}, Quilometragem= {self.kmi}km, {self.status})"
        
    def get_placa(self):
        return self.placa
    
    def get_valor(self):
        return self.valor
    
    def get_status(self):
        return self.status
    
    def set_status(self,status):
        self.status = status
    
    def get_nomecarro(self):
        return self.nome
    
    def set_kmi(self,kmi):
        self.kmi = kmi
    
    
    



    
        
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
    
    def get_historico(self):
        return self.historico
    
    def set_historico(self,historico):
        self.historico = historico


class Aluguel:
    def __init__(self, carro_alugado, pessoa_alugou, datai, dataf, valort, sts_pagamento): 
        self.carro_alugado = carro_alugado
        self.pessoa_alugou = pessoa_alugou
        self.datai = datai
        self.dataf = dataf
        self.valort = valort
        self.sts_pagamento = sts_pagamento
    
    def __str__(self):
        return f"Alugado: {self.carro_alugado}, Cliente: {self.pessoa_alugou}, Datas: {self.datai} até {self.dataf}, Valor total: {self.valort}, {self.sts_pagamento}."

    def get_pessoa_alugou(self):
        return self.pessoa_alugou 

    def get_valorpagar(self):
        return self.valort  

    def set_valorpagar(self, valort):
        self.valort = valort
    
    def get_placa_alugou(self):
        return self.carro_alugado

class SistemaAluguel:
    def __init__(self):
        pass

    def aluga(self, alg, lista_carros):
        
        carro_aux = next((carro for carro in lista_carros if carro.get_placa() == alg), None)

        if carro_aux:
            
            print(f"Veículo com placa {carro_aux.get_placa()} será alugado.")
            return carro_aux
        else:
            print("Veículo não encontrado no sistema. Tente novamente mais tarde.")
    
    def pagar(self, dias, esc):
        valorpagar = esc.get_valor()*dias
        print(f"O cliente terá que pagar R$ {valorpagar}")
        return valorpagar
    
    def devolucao_check(self,placa_dev, lista):
        
        dev_aux  = next((dev for dev in lista if dev.get_placa_alugou() == placa_dev), None)

        if dev_aux:
            print("Há um carro alugado com essa placa. Prosseguiremos aos próximos passos:")
            flag = True
        else:
            flag = False
            print("Não existe um processo ligado à essa placa. Tente novamente depois.")
        return dev_aux, flag
    
    def batida(self, alg, lista_carros):
        
        carro_aux = next((carro for carro in lista_carros if carro.get_placa() == alg), None)

        if carro_aux:
            carro_aux.set_status("Manutenção")
            print(f"Veículo com placa {carro_aux.get_placa()} foi para a manutenção.\nO valor será acertado com as partes posteriormente.")
            
        else:
            print("Veículo não encontrado no sistema. Tente novamente mais tarde.")

    def devolucao(self, alg, lista_carros):
        
        carro_aux = next((carro for carro in lista_carros if carro.get_placa() == alg), None)

        if carro_aux:
            carro_aux.set_status("Disponível")
            print(f"Veículo com placa {carro_aux.get_placa()} está novamente disponível para ser alugado.")
            
        else:
            print("Veículo não encontrado no sistema. Tente novamente mais tarde.")

    def hist(self, cpf, lista):

        client_aux = next((cliente for cliente in lista if cliente.get_cpf() == cpf), None)

    #def km
        
        


            
            


            
                



#VALUES ({self.nome}, {self.placa}, {self.cor}, {self.ano}, {self.marca}, {self.tipo}, {self.valor})