import sqlite3
from classes import Aluguel, Veiculo, Cliente

lista_carros = []

while True:
    print("Bem vindo ao sistema de aluguel de veículos, escolha uma opção desejada: ")
    print("1- Cadastrar um veículo para alugar")
    print("2- Alugar um veículo")
    print("5- Encerrar programa")
    op = int(input())
    
    match op:
        case 1:
            print("Você escolheu cadastrar um veículo!")
            c = Veiculo(input("Nome do carro: "), input("Placa: "), input("Cor: "), int(input("Ano de fabricação: ")), input("Marca: "), input("Categoria: "), float(input("Valor por dia: ")),"Disponível")
            c.cadastro()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        case 5:
            break
        case _:
            print("Opção inválida! Por favor análise as opções e escolha novamente.\n")

