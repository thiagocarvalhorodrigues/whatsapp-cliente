from tinydb import TinyDB, Query

banco = TinyDB('profile.json')
User = Query()

class bancodedados:
     def __init__(self,numero_da_conta):
          self.numero_da_conta = numero_da_conta

     def insert(self):

          banco.insert({'celular':self.pesquisa})


     def search(self):

          self.pesquisa = self.numero_da_conta
          print("Print - db.py",(self.pesquisa))

          resultado = banco.search(User.nome == (self.pesquisa))
          try:
               if self.pesquisa == str(resultado[0]['celular']):
                    print("Encontrado --->", resultado[0]['celular'],"----->",resultado)
          except:
               print("Não encontrado")
               self.insert()


# insert()
# search()
# print(banco.all())

