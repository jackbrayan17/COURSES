class Person:
    def __init__(self, name, cni_number, neighborhood, profession):
        self.name = name
        self.cni_number = cni_number
        self.neighborhood = neighborhood
        self.profession = profession

class Bank:
    list_of_banks=[]

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.number_of_clients = 0
        self.total_transactions = 0
        Bank.list_of_banks.append(self)

class Client:
    def __init__(self, person, bank):
        super().__init__(person.name, person.cni_number, person.neighborhood, person.profesion)
        self.bank = bank
        self.Account = []
        bank.number_of_clients += 1

    @classmethod
    def create_client(cls, name, cni_number, neighborhood, profesion, bank):
            person = Person(name, cni_number, neighborhood, profesion)