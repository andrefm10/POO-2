from classes import Aluguel, Veiculo, Cliente, SistemaAluguel
from datetime import datetime

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
    print("\nBem vindo ao sistema de aluguel de veículos, escolha uma opção desejada: ")
    print("1- Cadastrar um veículo para alugar")
    print("2- Cadastrar um cliente")
    print("3- Alugar/Relatório de aluguéis")
    print("4- Processo de devolução")
    print("5- Relatório do sistema")
    print("6- Realizar pagamento/manutenção")
    print("7- Encerrar programa")

    op = int(input())
    flag = False

    match op:
        case 1:
            print("Você escolheu cadastrar um veículo.") #transf em funcao
            print("Digite as informações necessárias a seguir: ")
            aux.cadastro_carro(lista_carros,aux)
            
        case 2:
            print("Você escolheu cadastrar um cliente.") #transf em funcao
            print("Digite as informações necessárias a seguir: ")
            aux.cadastro_cliente(lista_clientes, aux)

        case 3:
            opA = int(input("Escolha 1 se deseja realizar o processo do aluguel.\nEscolha 2 se deseja ver a lista de processos em andamento/pendentes.\n"))
            match opA:
                case 1:
                    print("Você escolheu alugar um carro.")
                    cpf_aluga = input("Digite o CPF que deseja alugar um carro: ")
                    
                    for i in lista_clientes: #transf em funcao
                        if cpf_aluga == i.get_cpf():
                            print(f"Certo. {i.get_nome()} está no sistema.")
                            print("Digite as informações necessárias a seguir: ") 
                            datai = input("Digite a data de retirada do veículo(dd/mm/aaaa): ")
                            dataf = input("Digite a data de entrega do veículo(dd/mm/aaaa): ")
                            data_i = datetime.strptime(datai, formato).date()
                            data_f = datetime.strptime(dataf, formato).date()
                            dias = (data_f-data_i).days
                            if dias == 0:
                                dias = 1
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
                    esc, flag= aux.aluga(alg, lista_carros)
                    if not flag:
                        continue
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
            aux.kmdev(placa_dev,kmnovo,lista_carros)
            
            atraso_bool = input("Houve atraso para a devolução? (S ou N): ").upper()
            match atraso_bool:
                case "S":
                    atraso_dias = int(input("Quantos dias de atraso?: "))
                    print(f"Nesse caso, o valor a pagar será de R$ {atraso_dias*50} como multa pelo atraso.")
                case "N":
                    print("Sem multa.")
                case _:
                    print("Opção inválida. Tente novamente depois.")
                    continue
            
            batida = input("Durante o período alugado, houve alguma acidente ou batida? (S ou N): ").upper()
            match batida:
                case "S":
                    aux.batida(placa_dev,lista_carros)
                    lista_alugueis.remove(dev)
                case "N":
                    aux.devolucao(placa_dev, lista_carros)
                    lista_alugueis.remove(dev)
                case _:
                    print("Digitação inválida.")
                    continue
            aux.hist(cpf_dev, lista_clientes)
        
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
            print("Escolha uma das opções a seguir:")
            print("1- Pagar pendência")
            print("2- Realizar manutenção")           
            opB = int(input())

            match opB:
                case 1:
                    plc = input("Digite a placa do carro que está com pagamento pendente: ")
                    aux.pagamento(plc,lista_alugueis, lista_carros)

                case 2:
                    print("Veja os carros da frota que estão em manutenção")
                    for i in lista_carros: 
                        if i.get_status() == "Manutenção" :
                            print(i)
                    man = input("Digite a placa do carro que deseja realizar a manutenção: ")
                    aux.arrumar(man,lista_carros)



        case 7:
            break
        case _:
            print("Opção inválida! Por favor análise as opções e escolha novamente.")

