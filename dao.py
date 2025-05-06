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

DaoCategory.save('Frutas')
DaoCategory.save('Verduras')
DaoCategory.save('Legumes')
DaoCategory.read()