class Funcionario:
    def __init__(self, nome, id):
        self.nome = nome 
        self.id = id
    def get_nome(self):
        return self.nome
    def get_id(self):
        return self.id

class Gerente:
    def __init__(self, nome, id, secao):
        self.nome = nome 
        self.id = id
        self.secao = secao
    def get_sec(self):
        return self.secao

class Assistente(Funcionario):
    def __init__(self, nome, id, hab):
        super().__init__(nome, id) 
        self.hab = hab
    def get_hab(self):
        return self.hab
    
listaf = []
f1 = Funcionario("Davi", 1)
listaf.append(f1)

while True:
    print("Selecione as opções:\n1-Criar funcionario\n2-Exibir dados\n3- Fim")
    op = int(input())



    if op == 1:
        f = Funcionario(input(),int(input()))
        listaf.append(f)
    
    if op == 2:
        opp = (input())
        for i in listaf:
            if opp == i.get_nome():
                print(f"Nome: {i.get_nome()}")
                print(f"id: {i.get_id()}")
    
    if op == 3:
        break


        