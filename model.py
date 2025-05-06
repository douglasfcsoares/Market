from datetime import datetime

class Category: # Categoria
    def __init__(self, category):
        self.category = category

class Products: # Produtos
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Stock: # Estoque
    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity

class Sale: # Vendas
    def __init__(self, soldItems: Products, salesPerson, buyer, quantitySold, date = datetime.now()):
        self.soldItems = soldItems
        self.salesPerson = salesPerson
        self.buyer = buyer
        self.quantitySold = quantitySold
        self.date = date

class Supplier: # Fornecedor
    def __init__(self, name, cnpj, phone, category):
        self.name = name
        self.phone = phone
        self.cnpj = cnpj
        self.category = category

class Person:
    def __init__(self, name, phone, cpf, email, address):
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email
        self.address = address

class Employee(Person): # Funcionário
    def __init__(self, clt, position, name, phone, cpf, email, address):
        self.clt = clt
        self.position = position # Cargo do funcionário
        super().__init__(name, phone, cpf, email, address)