from model import Category, Employee, Person, Products, Sale, Stock, Supplier
from dao import DaoCategory, DaoEmployee, DaoProduct, DaoPerson, DaoSale, DaoSupplier, DaoStock
from datetime import datetime

class ControllerCategory:
    def addCategory(self, newCategory):
        contains = False
        dao = DaoCategory.read()
        for i in dao:
            if i.category == newCategory:
                contains = True

        if not contains:
            DaoCategory.save(newCategory)
            print('Categoria adicionada com sucesso!')
        else:
            print('Categoria já existe!')

    def deleteCategory(self, delCategory):
        dao = DaoCategory.read()
        category = list(filter(lambda dao: dao.category == delCategory, dao))

        if len(category) <= 0:
            print('A categoria que deseja deletar não existe.')
        else:
            for i in category:
                if dao[i].category == delCategory:
                    del dao[i]
                    break
            print('Categoria removida com sucesso.')

            with open('category.txt', 'w') as arq:
                for i in dao:
                    arq.write(dao[i].category + '\n')

    def renameCategory(self, oldCategory, newCategory):
        dao = DaoCategory.read()
        category = list(filter(lambda dao: dao.category == oldCategory, dao))
        if len(category) > 0:
            category1 = list(filter(lambda dao: dao.category == oldCategory, dao))
            if len(category1) == 0:
                dao = list(map(lambda dao: Category(oldCategory) if(dao.category == newCategory) else(dao), dao))
                print('A categoria foi alterada com sucesso.')
            else:
                print('A categoria que deseja alterar não existe.')
        else:
            print('A categoria que deseja alterar não exiaste.')

        with open('category.txt', 'w') as arq:
            for i in dao:
                arq.writelines(i.category)
                arq.writelines('\n')


a = ControllerCategory()
a.renameCategory('Frutas', 'Carnes')

