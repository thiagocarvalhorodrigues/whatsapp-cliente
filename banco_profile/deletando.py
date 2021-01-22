from banco_profile.db import bancodedados
import shutil
import PySimpleGUI as sg

class deletar:

    def __init__(self,chave):
        self.chave = chave


    def delete(self):
        try:
            return bancodedados.banco.remove(bancodedados.User.celular == self.chave) and shutil.rmtree(f'profiles/{self.chave}')
        except:
            sg.Popup("Não possui nenhum arquivo Profile ou arquivo no banco de dados a ser excluído")