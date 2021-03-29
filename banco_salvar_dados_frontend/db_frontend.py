from tinydb import TinyDB, Query


class BancoGuardarFrontend:
     banco = TinyDB('banco_salvar_dados_frontend\\banco_frontend.json')
     User = Query()

     def __init__(self,saudacao,resposta,resposta_condicional1,respostas_escutar_positiva,resposta_escutar_negativa,replica_negativa):
          self.saudacao = saudacao
          self.resposta = resposta
          self.resposta_condicional1 = resposta_condicional1
          self.resposta_escutar_positiva = respostas_escutar_positiva
          self.resposta_escutar_negativa= resposta_escutar_negativa
          self.replica_negativa = replica_negativa



     # def insert(self):
     #      print(self.quantidade_contato)
     #      self.banco.insert({'contato':self.quantidade_contato})


     def Update(self):
          self.banco.update({'saudacao':str(self.saudacao)})
          self.banco.update({'resposta': self.resposta})
          self.banco.update({'resposta_condicional1': self.resposta_condicional1})
          self.banco.update({'resposta_escutar_positiva': self.resposta_escutar_positiva})
          self.banco.update({'resposta_escutar_negativa': self.resposta_escutar_negativa})
          self.banco.update({'replica': self.replica_negativa})



     def select_all(self):
          return self.banco.all()
