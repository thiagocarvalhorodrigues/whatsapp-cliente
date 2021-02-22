from tinydb import TinyDB, Query


class banco_envio_contatos:
     banco = TinyDB('banco_enviar_quantidade_de_contatos\\banco_envio_contatos.json')
     User = Query
     def __init__(self,quantidade_contato):
          self.quantidade_contato =quantidade_contato


     def insert(self):
          print(self.quantidade_contato)
          self.banco.insert({'contato':int(self.quantidade_contato)})


     def Update(self):
          self.banco.update({'contato':int(self.quantidade_contato)})


     def select_all(self):
           return self.banco.all()