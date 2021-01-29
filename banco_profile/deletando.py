from banco_profile.db import bancodedados
import shutil
import PySimpleGUI as sg
import os
from pathlib import Path

class deletar:

    def __init__(self,chave):
        self.chave = chave


    def delete(self):
        try:
            return bancodedados.banco.remove(bancodedados.User.celular == self.chave) and shutil.rmtree(f'profiles\{self.chave}')
        except:
            sg.Popup("Não possui nenhum arquivo Profile e / OU arquivo no banco de dados a ser excluído")



    def deletar_todos_os_profile(self):

        try:
            json = (bancodedados.caminho_profile)
            with open(json,'w'):
                shutil.rmtree('profiles', ignore_errors=False, onerror=None)
                sg.Popup("Excluido")
        except:
            sg.Popup("Não possui nenhum arquivo Profile e / OU arquivo no banco de dados a ser excluído")