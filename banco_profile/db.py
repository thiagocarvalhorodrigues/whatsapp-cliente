from tinydb import TinyDB, Query

class bancodedados:
     banco = TinyDB('banco_profile/profile.json')
     User = Query()

     def __init__(self,numero_da_conta):
          self.numero_da_conta = numero_da_conta





     def insert(self):

          self.banco.insert({'celular':self.pesquisa})


     def search_insert(self):

          self.pesquisa = self.numero_da_conta
          resultado = self.banco.search(self.User.celular == self.pesquisa)
          try:
               if self.pesquisa == (resultado[0]['celular']):
                    print("Encontrou o valor")
          except:
               print("Não encontrado")
               self.insert()


     def encontrado(self):
          self.pesquisa = self.numero_da_conta
          try:
               resultado = self.banco.search(self.User.celular == self.pesquisa)
               pesquisa_certa = (resultado[0]['celular'])
               if self.pesquisa == pesquisa_certa:
                    return pesquisa_certa


                    # print(self.pesquisa,"pesquisa ")

          except:
               pass


     def select_all(self):
           return self.banco.all()

    ##### Não está sendo utilizando no momento #####
     def delete(self):
          return self.banco.remove(self.User.celular == self.chave)






