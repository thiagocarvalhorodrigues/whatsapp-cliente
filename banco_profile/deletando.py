from banco_profile.db import bancodedados


class deletar:

    def __init__(self,chave):
        self.chave = chave

    def delete(self):
        return bancodedados.banco.remove(bancodedados.User.celular == self.chave)



