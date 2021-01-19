from tinydb import TinyDB, Query
banco = TinyDB('profile.json')
User = Query()


def insert():

     banco.insert({'nome':'Joao', 'idade':33})
     banco.insert({'nome':'Vitor', 'idade':36})

def search():
     pesquisa =('Joao')

     resultado = banco.search(User.nome == (pesquisa))
     for i in resultado:
          if i['nome'] == pesquisa:
               print(i)









# insert()
search()
# print(banco.all())

