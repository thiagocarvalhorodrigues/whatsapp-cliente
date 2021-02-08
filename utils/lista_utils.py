import PySimpleGUI as sg
from banco_enviar_quantidade_de_contatos import db_envio_contatos

class ListaUtils:

    def __init__(self):
        pass

    def particionar_lista(lista, n):
        inicio = 0
        for i in range(n):
            final = inicio + len(lista[i::n])
            yield lista[inicio:final]
            inicio = final



    def limpar_espacos_em_brancos(listao):
        return [int(item) for item in listao if item.isdigit()]



    def menu_enviar_contatos(self):


        select_dados = db_envio_contatos.banco_envio_contatos(quantidade_contato='0')
        select_quantidade_dos_quantidades = select_dados.select_all()
        print(select_quantidade_dos_quantidades)
        print(int(select_quantidade_dos_quantidades[0]['contato']))

        layoutmenu = [
            [sg.Text('Informe a quantidade de contatos por envio', background_color='#3CB371', text_color='#FFFAFA')],
            [sg.Input((int(select_quantidade_dos_quantidades[0]['contato'])), key='envio_quantidade_de_contatos')],
            [sg.OK('Salvar')]

            ]
        janela = sg.Window("Configuração de envio de mensagens", layoutmenu, button_color=('#FFFAFA', '#FF4500'),
                           background_color='#3CB371', icon='recursos/imagens/icone.ico', alpha_channel=0.9).Finalize()

        while True:

            event, valores = janela.read()
            if event in (None, 'Close Window'):
                janela.close()
                break

            arquivo_menu_enviar_contatos = (valores['envio_quantidade_de_contatos'])

            if event == 'Salvar':
                banco_envio_quantidade_contatos = db_envio_contatos.banco_envio_contatos(quantidade_contato=arquivo_menu_enviar_contatos)
                banco_envio_quantidade_contatos.Update()
                janela.close()