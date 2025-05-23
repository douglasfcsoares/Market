from model import *

class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as arq:
            arq.writelines(category)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('category.txt', 'r') as arq:
            cls.category = arq.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))
        cat = []
        for i in cls.category:
            cat.append(Category(i))
        return cat

class DaoProduct:
    @classmethod
    def save(cls, product: Products):
        with open('product.txt', 'a') as arq:
            arq.writelines(product.name + '|' + product.price + '|' + product.category)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('product.txt', 'r') as arq:
            cls.product = arq.readlines()
        cls.product = list(map(lambda x: x.replace('\n', ''), cls.product))
        cls.product = list(map(lambda x: x.split('|'), cls.product))
        pro = []
        for i in cls.product:
            pro.append(Products(i[0], i[1], i[2]))
        return pro

class DaoStock:
    @classmethod
    def save(cls, stock: Stock):
        with open('stock.txt', 'a') as arq:
            arq.writelines(stock.product + '|' + stock.quantity)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('stock.txt', 'r') as arq:
            cls.stock = arq.readlines()
            cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
            cls.stock = list(map(lambda x: x.split('|'), cls.stock))

            sto = []
            if len(cls.stock) > 0:
                for i in cls.stock:
                    sto.append(Stock(Products(i[0], i[1], i[2], i[3])))
            return sto

class DaoSale:
    @classmethod
    def save(cls, sale: Sale):
        with open('sale.txt', 'a') as arq:
            arq.writelines(sale.soldItems.name + '|' + 
                        sale.soldItems.price + '|' + 
                        sale.soldItems.category + '|' + 
                        sale.salesPerson + '|' + 
                        sale.buyer + '|' + 
                        str(sale.quantitySold) + '|' + 
                        sale.date)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('sale.txt', 'r') as arq:
            cls.sale = arq.readlines()

        cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
        cls.sale = list(map(lambda x: x.split('|'), cls.sale))
        sales = []
        for i in cls.sale:
            sales.append(Sale(Products(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return sales

class DaoSupplier:
    @classmethod
    def save(cls, supplier: Supplier):
        with open('supplier.txt', 'a') as arq:
            arq.writelines(supplier.name + '|' + supplier.phone + '|' + supplier.cnpj + '|' + supplier.category)
            arq.writelines('\n')
    @classmethod
    def read(cls):
        with open('supplier.txt', 'r') as arq:
            cls.supplier = arq.readlines()
            cls.supplier = list(map(lambda x: x.replace('\n', ''), cls.supplier))
            cls.supplier = list(map(lambda x: x.split('|'), cls.supplier))
            sup = []
            for i in cls.supplier:
                sup.append(Supplier(i[0], i[1], i[2], i[3]))
            return sup

class DaoPerson:
    @classmethod
    def save(cls, person: Person):
        with open('person.txt', 'a') as arq:
            arq.writelines(person.name + '|' + person.phone + '|' + person.cpf + '|' + person.email + '|' + person.address)
            arq.writelines('\n')
    @classmethod
    def read(cls):
        with open('person.txt', 'r') as arq:
            cls.person = arq.readlines()
            cls.person = list(map(lambda x: x.replace('\n', ''), cls.person))
            cls.person = list(map(lambda x: x.split('|'), cls.person))

            pers = []
            for i in cls.person:
                pers.append(Person(i[0], i[1], i[2], i[3], i[4]))
            return pers

class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open('employee.txt', 'a') as arq:
            arq.writelines(employee.clt + '|' + employee.name + '|' + employee.phone + '|' + employee.cpf + '|' + employee.email + '|' + employee.address)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('employee.txt', 'r') as arq:
            cls.employee = arq.readlines()
            cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
            cls.employee = list(map(lambda x: x.split('|'), cls.employee))
            
            employees = []
            for i in cls.employee:
                employees.append(Employee(i[0], i[1], i[2], i[3], i[4, i[5]]))
            return employees
