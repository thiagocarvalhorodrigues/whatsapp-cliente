from tinydb import TinyDB, Query
from logs.whats_log import funcao_info

class bancodedados:

     banco = TinyDB('banco_profile\profile.json')
     caminho_profile = 'banco_profile\profile.json'
     User = Query()

     def __init__(self,numero_da_conta):
          self.numero_da_conta = numero_da_conta


     def insert(self):
          self.banco.insert({'celular':self.numero_da_conta})


     def search_insert(self):
          resultado = self.banco.search(self.User.celular == self.numero_da_conta)
          try:
               if len(resultado) > 0:
                    print("Encontrou o valor")
               else:
                    print("Não encontrado")
                    self.insert()
          except:
               self.insert()
               # print(ex)
               # funcao_info('DENTRO DA FUNÇÃO search_insert, NÃO ENCONTROU O NÚMERO DA CONTA DENTRO DO BANCO DE DADOS E ADICIONOU.')


     def encontrado(self):
          try:
               resultado = self.banco.search(self.User.celular == self.numero_da_conta)
               pesquisa_certa = (resultado[0]['celular'])
               if self.numero_da_conta == pesquisa_certa:
                    return pesquisa_certa


          except:
               pass
               # funcao_info('DENTRO DA FUNÇAO encontrado, O VALOR NÃO FOI ENCONTRADO DENTRO DO BANCO DE DADOS')


     def select_all(self):
           return self.banco.all()