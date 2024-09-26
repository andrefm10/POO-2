from classes import Aluguel, Veiculo, Cliente, SistemaAluguel
from datetime import datetime

def verifica_placa(lista_carros, placa):
        for p in lista_carros:
            while placa == p.get_placa():
                 placa = input("Essa placa já está na frota de carros, por favor digite corretamente: ")
        return placa

def verifica_cpf(lista_clientes, cpf):
        for i in lista_clientes:
            while cpf == i.get_cpf():
                 cpf = input("Esse(a) cliente já está cadastrado no sistema, por favor digite o CPF corretamente: ")
        return cpf

def verifica_tel(lista_clientes, tel):
        for i in lista_clientes:
            while tel == i.get_tel():
                 tel = input("Esse(a) cliente já está cadastrado no sistema, por favor digite o telefone corretamente: ")
        return tel

def verifica_email(lista_clientes, email):
        for i in lista_clientes:
            while email == i.get_email():
                 email = input("Esse(a) cliente já está cadastrado no sistema, por favor digite o e-mail corretamente: ")
        return email

def verifica_cnh(lista_clientes, cnh):
        for i in lista_clientes:
            while cnh == i.get_cnh():
                 cnh = input("Esse(a) cliente já está cadastrado no sistema, por favor digite o número da CNH corretamente: ")
        return cnh


lista_carros = []

v = Veiculo("Uno","ABC-1234", "Preto", "2020","Fiat", "Hatch", 130, 60000, "Disponível")
lista_carros.append(v)
v= Veiculo("Kwid", "HFM-7421", "Branco","2019","Renault","Hatch", 120, 70000, "Manutenção")
lista_carros.append(v)

lista_clientes = []

c = Cliente("André", "13182036947", "48999985432", "andrefilipmartins@gmail.com", "123456789", 0)
lista_clientes.append(c)

formato = "%d/%m/%Y"

while True:
    print("Bem vindo ao sistema de aluguel de veículos, escolha uma opção desejada: ")
    print("1- Cadastrar um veículo para alugar")
    print("2- Cadastrar um cliente")
    print("5- Encerrar programa")
    op = int(input())
    flag = False

    match op:
        case 1:
            print("Você escolheu cadastrar um veículo.")
            print("Digite as informações necessárias a seguir: ")
            nome_carro = input("Nome do carro: ")
            placa = input("Placa: ")
            placa = verifica_placa(lista_carros,placa)
            cor = input("Cor: ")
            ano = input("Ano de fabricação: ")
            marca = input("Marca: ")
            cat = input("Categoria: ")
            valor = float(input("Valor por dia: "))
            kmi = int(input("Digite a quilometragem do carro: "))
            vi = Veiculo(nome_carro, placa, cor, ano, marca, cat, valor, kmi, "Disponível")
            lista_carros.append(vi)

            print("Veículo cadastrado no sistema com sucesso!\n")
        
        case 2:
            print("Você escolheu cadastrar um cliente.")
            print("Digite as informações necessárias a seguir: ")
            nome_cliente = input("Nome: ")
            cpf = input("CPF(Sem traços): ")
            cpf = verifica_cpf(lista_clientes,cpf)
            tel = input("Telefone(Sem traços): ")
            tel = verifica_tel(lista_clientes,tel)
            email = input("E-mail: ") 
            email = verifica_email(lista_clientes, email)
            cnh = input("Número da CNH: ")
            cnh = verifica_cnh(lista_clientes, cnh)
            ci = Cliente(nome_cliente, cpf, tel, email, cnh, 0 )
            lista_clientes.append(ci)

            print("Cliente cadastrado no sistema com sucesso!\n")

        case 3:
            print("Você escolheu alugar um carro.")
            cpf_aluga = input("Digite o CPF que deseja alugar um carro: ")
            
            for i in lista_clientes:
                if cpf_aluga == i.get_cpf():
                    print(f"Certo. {i.get_nome()} está no sistema.")
                    print("Digite as informações necessárias a seguir: ")
                    datai = input("Digite a data de retirada do veículo(dia/mês/ano): ")
                    dataf = input("Digite a data de entrega do veículo(dia/mês/ano): ")
                    data_i = datetime.strptime(datai, formato).date()
                    data_f = datetime.strptime(dataf, formato).date()
                    dias = (data_f-data_i).days
                    flag=True
            if not flag:
                print("O CPF digitado não existe no sistema, tente novamente: ")
                continue
            print("Dê uma olhada nos carros disponíveis: ")
            for i in lista_carros:
                if i.get_status() == "Disponível" :
                    print(i)
            alg = input("Agora, digite o nome do carro que deseja alugar: ")
            aluguel()
            
                

            


            
            
              



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        case 5:
            break
        case _:
            print("Opção inválida! Por favor análise as opções e escolha novamente.\n")

