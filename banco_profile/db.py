from tinydb import TinyDB, Query
from logs.whats_log import funcao_info

class bancodedados:
     banco = TinyDB('banco_profile\profile.json')
     caminho_profile = 'banco_profile\profile.json'
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
               funcao_info('DENTRO DA FUNÇÃO search_insert, NÃO ENCONTROU O NÚMERO DA CONTA DENTRO DO BANCO DE DADOS E ADICIONOU.')


     def encontrado(self):
          self.pesquisa = self.numero_da_conta
          try:
               resultado = self.banco.search(self.User.celular == self.pesquisa)
               pesquisa_certa = (resultado[0]['celular'])
               if self.pesquisa == pesquisa_certa:
                    return pesquisa_certa


          except:
               pass
               # funcao_info('DENTRO DA FUNÇAO encontrado, O VALOR NÃO FOI ENCONTRADO DENTRO DO BANCO DE DADOS')


     def select_all(self):
           return self.banco.all()