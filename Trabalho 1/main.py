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

aux = SistemaAluguel()
lista_alugueis = []
lista_carros = []
lista_clientes = []

v = Veiculo("Uno","ABC-1234", "Preto", "2020","Fiat", "Hatch", 130, 60000, "Disponível")
lista_carros.append(v)
v= Veiculo("Kwid", "HFM-7421", "Branco","2019","Renault","Hatch", 120, 70000, "Manutenção")
lista_carros.append(v)

c = Cliente("André", "13182036947", "48999985432", "andrefilipmartins@gmail.com", "123456789", 0)
lista_clientes.append(c)

formato = "%d/%m/%Y"

while True:
    print("Bem vindo ao sistema de aluguel de veículos, escolha uma opção desejada: ")
    print("1- Cadastrar um veículo para alugar")
    print("2- Cadastrar um cliente")
    print("3- Processo de aluguel")

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
            opA = int(input("Escolha 1 se deseja realizar o processo do aluguel.\nEscolha 2 se deseja ver a lista de processos em andamento/pendentes.\n"))
            match opA:
                case 1:
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
                            clienteaux = i
                    if not flag:
                        print("O CPF digitado não existe no sistema, tente novamente: ")
                        continue
                    print("Aqui estão os carros disponíveis: ")
                    for i in lista_carros:
                        if i.get_status() == "Disponível" :
                            print(i)
                    alg = input("Agora, digite a placa do carro que será alugado: ")
                    esc = aux.aluga(alg, lista_carros)

                    print("Ok. Prossiga agora para o pagamento: ")
                    valorpagar = aux.pagar(dias,esc)
                    pgmt = input("Pagamento já foi realizado? (S ou N)").upper()
                    match pgmt:
                        case "S":
                            esc.set_status("Alugado")
                            a = Aluguel(esc.get_placa(), clienteaux.get_cpf(), datai, dataf,valorpagar,"Pago")
                            lista_alugueis.append(a)
                            print("Processo de aluguel feito com sucesso.\n")

                        case "N":
                            esc.set_status("Pendente")
                            print("Como não houve pagamento ainda, o aluguel ficará pendente até a realização do pagamento.")
                            a = Aluguel(esc.get_placa(), clienteaux.get_cpf(), datai, dataf,valorpagar,"Pendente")
                            lista_alugueis.append(a)
                        case _:
                            print("Opção inválida. Tente novamente depois.")
                case 2:
                    if len(lista_alugueis) == 0:
                        print("Ainda não existe nenhum processo em andamento ou pendente.")
                    else:
                        for i in lista_alugueis:
                            print(i)
                case _:
                    print("Opção inválida. Tente novamente depois.")
            
        case 4:
            print("Você escolheu realizar a devolução de um veículo.")
            print("Por favor, responda as questões a seguir: ")
            placa_dev = input("Digite a placa do carro que será devolvido à frota: ")
            cpf_dev = input("Digite o CPF cadastrado no aluguel em questão: ")
            dev, flag = aux.devolucao_check(placa_dev, lista_alugueis)
            if not flag:
                continue
            kmnovo = int(input("O veículo está com quantos quilômetros rodados agora?: "))
            
            
            atraso_bool = input("Houve atraso para a devolução? (S ou N): ").upper()
            match atraso_bool:
                case "S":
                    atraso_dias = int(input("Quantos dias de atraso?: "))
                    print(f"Nesse caso, o valor a pagar será de R$ {atraso_dias*50} como multa pelo atraso.")
                case "N":
                    print("Sem multa.")
                case _:
                    print("Digitação inválida.")
                    continue
            batida = input("Durante o período alugado, houve alguma acidente ou batida? (S ou N): ").upper()
            match batida:
                case "S":
                    aux.batida(placa_dev,lista_carros)
                    lista_alugueis.pop(esc)
                case "N":
                    aux.devolucao(placa_dev, lista_carros)
                    lista_alugueis.pop(esc)
                case _:
                    print("Digitação inválida.")
                    continue
        
        case 5:
            print("Você selecionou o relatório do sistema:\n")
            print("Carros da frota:")
            if len(lista_carros) == 0:
                    print("A frota de carros está vazia.")
            else:
                for i in lista_carros:
                    print(i)
            print("\nClientes cadastrados: ")
            if len(lista_clientes) == 0:
                    print("Não há cliente cadastrado.")
            else:
                for i in lista_clientes:
                    print(i)

            

            

                    
                    




            
            
                

            


            
            
              



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        case 6:
            break
        case _:
            print("Opção inválida! Por favor análise as opções e escolha novamente.\n")

