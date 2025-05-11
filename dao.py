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

# DaoCategory.save('Frutas')
# DaoCategory.save('Verduras')
# DaoCategory.save('Legumes')
# DaoCategory.read()

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

x = DaoSale.read()
print(x[0].soldItems.name)