import sqlite3

cx = sqlite3.connect("aluguel.db")

cr = cx.cursor()

cr.execute('''
CREATE TABLE IF NOT EXISTS carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    placa TEXT NOT NULL,
    cor TEXT NOT NULL,
    ano INTEGRER,
    marca TEXT NOT NULL,
    tipo TEXT NOT NULL,
    valor REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'Disponível' 
)
''')

carross = [
    ("Civic", "ABC-1234", "Prata", 2018, "Honda", "Sedan", 150.00),
    ("Compass", "DEF-5678", "Preto", 2020, "Jeep", "SUV", 200.00),
    ("Mobi", "GHI-9101", "Branco", 2016, "Fiat", "Hatch", 100.00),
    ("Corolla", "JKL-1213", "Azul", 2018, "Toyota", "Sedan", 170.00),
    ("Onix", "MNO-1415", "Vermelho", 2017, "Chevrolet", "Hatch", 120.00),
    ("EcoSport", "PQR-1617", "Cinza", 2020, "Ford", "SUV", 180.00),
    ("Duster", "STU-1819", "Preto", 2021, "Renault", "SUV", 190.00),
    ("Kicks", "VWX-2021", "Verde", 2022, "Nissan", "SUV", 210.00),
    ("Gol", "YZA-2223", "Prata", 2016, "Volkswagen", "Hatch", 110.00),
    ("HB20", "BCD-2425", "Azul", 2017, "Hyundai", "Hatch", 130.00),
    ("Tracker", "EFG-2627", "Vermelho", 2022, "Chevrolet", "SUV", 220.00),
    ("208", "HIJ-2829", "Branco", 2018, "Peugeot", "Hatch", 125.00),
    ("Toro", "KLM-3031", "Preto", 2020, "Fiat", "Pickup", 230.00),
    ("T-Cross", "NOP-3233", "Cinza", 2022, "Volkswagen", "SUV", 240.00),
    ("Hilux", "QRS-3435", "Vermelho", 2020, "Toyota", "Pickup", 250.00),
    ("Renegade", "TUV-3637", "Verde", 2019, "Jeep", "SUV", 200.00),
    ("Cruze", "WXY-3839", "Azul", 2018, "Chevrolet", "Sedan", 170.00),
    ("Kwid", "ZAB-4041", "Branco", 2015, "Renault", "Hatch", 105.00),
    ("Ranger", "CDE-4243", "Prata", 2020, "Ford", "Pickup", 260.00),
    ("HR-V", "FGH-4445", "Preto", 2019, "Honda", "SUV", 210.00)
]

cr.executemany('''
INSERT INTO carros (nome, placa, cor, ano, marca, tipo, valor) 
VALUES (?, ?, ?, ?, ?, ?, ?)
''', carross)

def listar_carros_disponiveis():

    cr.execute('SELECT * FROM carros WHERE status = 1 ')
    carros = cr.fetchall()

    print("Carros disponíveis para aluguel:")
    for carro in carros:
        print(f"ID: {carro[0]} - Nome: {carro[1]} - Placa: {carro[2]} - Cor: {carro[3]} - Marca: {carro[4]} - Tipo: {carro[5]} - Valor Diário: R${carro[6]:.2f} - Ano: {carro[8]}")


cx.commit()

cr.execute('SELECT * from carros')
cars = cr.fetchall()

for i in cars:
    print(i)

cx.close()

