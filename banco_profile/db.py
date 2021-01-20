from tinydb import TinyDB, Query

banco = TinyDB('banco_profile\profile.json')
User = Query()

class bancodedados:

     def __init__(self,numero_da_conta):
          self.numero_da_conta = numero_da_conta



     def insert(self):

          banco.insert({'celular':self.pesquisa})


     def search_insert(self):

          self.pesquisa = self.numero_da_conta
          resultado = banco.search(User.celular == self.pesquisa)
          try:
               if self.pesquisa == (resultado[0]['celular']):
                    print("Encontrou o valor")
          except:
               print("Não encontrado")
               self.insert()

     def encontrado(self):
          self.pesquisa = self.numero_da_conta
          try:
               pesquisa = self.pesquisa
               resultado = banco.search(User.celular == pesquisa)
               pesquisa_certa = (resultado[0]['celular'])
               if pesquisa == pesquisa_certa:
                    print(pesquisa,"pesquisa ")

          except:
               pass



