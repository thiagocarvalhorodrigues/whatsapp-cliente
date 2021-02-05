import PySimpleGUI as sg
import csv
from threadd.thread_manager import send_msg_thread, configure_qrcode_thread, verify_msg_thread
from threading import Thread
from banco_profile import db
import shutil
from banco_profile.deletando import deletar
import os.path
import os
from utils.lista_utils import ListaUtils

dir_path = os.getcwd()
sg.theme('TanBlue')
background_fundo = '#FF4500'
background_fonte = '#FFFAFA'


menu_tela_inicial = [
    ['Ajuda',[ 'Versão','Tutorial']],
    ['Contato',['Sobre']]

    ]
layout12 = [[sg.Image('recursos/imagens/convertido1100px.png')],

]

layout =    [[sg.Menu(menu_tela_inicial)],
            [sg.Button('Configurar QRCode',button_color=(background_fonte,background_fundo), key='configurar'), sg.Button('Remover QRCode', button_color=(background_fonte,background_fundo), key='remover')],
            [sg.Text('Arquivo de Entrada ( números a serem disparados)  CSV:',text_color=background_fonte, background_color='#3CB371', font=('Arial', 10, 'bold'))],
            [sg.Input(key='csv'), sg.FileBrowse(button_text='Pesquisa', button_color=(background_fonte,background_fundo), key='file',target='csv')],
            [sg.Text('Arquivo de Saída EXCEL:',text_color=background_fonte, background_color='#3CB371', font=('Arial', 10, 'bold'))],
            [sg.Text('( Armazena os dados dos clientes ) que aceitaram a CAMPANHA: ',text_color=background_fonte, background_color='#3CB371',)],
            [sg.Input(key='excel'), sg.FileBrowse(button_text='Pesquisar',button_color=(background_fonte,background_fundo), key='saida', target='excel')],
            [sg.Text('ARQUIVO/FOTO/VIDEO -- Selecione para SAUDAÇÃO:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold'))],
            [sg.Input(key='foto'), sg.FileBrowse(button_text='Pesquisar',button_color=(background_fonte,background_fundo), key='arquivo', target='foto')],
            [sg.Text('ARQUIVO/FOTO/VIDEO -- Selecione para RESPOSTA:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold'))],
            [sg.Input(key='foto_resposta'), sg.FileBrowse(button_text='Pesquisar',button_color=(background_fonte,background_fundo), key='arquivo_resposta', target='foto_resposta')],
            [sg.Text('LEGENDA DA FOTO Não obrigatório:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold')), sg.Text('Saudação:                                       ', text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold')),sg.Text('Resposta:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold'))],
            [sg.Multiline(size=(30,2),key='legenda'), sg.Multiline(size=(30, 2), key='textbox'),sg.Multiline(size=(30, 2), key='response')],
            [sg.Text('Resposta Condicional 1:                      Respostas para ESCUTAR - POSITIVA:  Respostas para ESCUTAR - NEGATIVA:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold'))],
            [sg.Multiline(size=(30, 2), key='resposta_cond_1'),sg.Multiline(size=(30, 2), key='escuta_positiva'),sg.Multiline(size=(30, 2), key='escuta_negativa')],
            [sg.Text('Réplica NEGATIVA:',text_color=background_fonte, background_color='#3CB371',font=('Arial', 10, 'bold'))],[sg.Text('A Réplica serve para responder uma posição NEGATIVA do cliente.',text_color=background_fonte, background_color='#3CB371',)],
            [sg.Multiline(size=(30, 2), key='replica_negativa')],
            [sg.Button('Iniciar', button_color=(background_fonte,background_fundo), key='iniciar'), sg.Button('Responder', button_color=(background_fonte,background_fundo), key='responder'),sg.Text('                  ', background_color='#3CB371', key='status')]]



dados = db.bancodedados(numero_da_conta='0')
(select_dos_numeros_cadastrados) = (dados.select_all())

posicao1 = None
posicao2 = None
posicao3 = None
posicao4 = None
posicao5 = None
posicao6 = None
posicao7 = None
posicao8 = None
posicao9 = None
posicao10 = None

for telefone in range(len(select_dos_numeros_cadastrados)):
    if telefone == 0:
        posicao1 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 1:
        posicao2 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 2:
        posicao3 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 3:
        posicao4 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 4:
        posicao5 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 5:
        posicao6 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 6:
        posicao7 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 7:
        posicao8 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 8:
        posicao9 = (select_dos_numeros_cadastrados[telefone]['celular'])
    if telefone == 9:
        posicao10 = (select_dos_numeros_cadastrados[telefone]['celular'])




layout2 = [ [sg.Text("Números no qual deseja enviar as mensagens", text_color=background_fonte, background_color='#3CB371', font=('Arial',10, 'bold'))],
        [sg.Text("1º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(posicao1, key="n1",size=(13,1))],
        [sg.Text("2º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(posicao2, key="n2",size=(13, 1))],
        [sg.Text("3º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(posicao3,key="n3",size=(13, 1))],
        [sg.Text("4º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(posicao4,key="n4",size=(13, 1))],
        [sg.Text("5º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12)),sg.Text("          ", background_color='#3CB371'), sg.Button('Excluir QRCode Indivídual',button_color=(background_fonte,background_fundo), key='botao_excluir_individual')],
        [sg.Input(posicao5,key="n5",size=(13, 1)),sg.Text("                ", background_color='#3CB371'),  sg.Input(key="input_excluir_individual",size=(10,1))],
        [sg.Text("6º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12)), sg.Text("                       Ex: 991938533",text_color=background_fonte,background_color='#3CB371')],
        [sg.Input(posicao6,key="n6",size=(13, 1))],
        [sg.Text("7º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(posicao7,key="n7",size=(13, 1))],
        [sg.Text("8º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(posicao8,key="n8",size=(13, 1))],
        [sg.Text("9º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(posicao9,key="n9",size=(13, 1))],
        [sg.Text("10º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(posicao10,key="n10",size=(13, 1))]]






layout_principal = [
    [sg.Column(layout12,expand_x='False',expand_y='False')],
    # [sg.Frame('',layout12)],
    # [sg.Frame("Configurações de envio de mensagens",layout2, background_color='#3CB371',border_width='3px', title_color='#000000'),sg.Frame('Acões',layout, background_color='#3CB371', border_width='3px', title_color='#000000', size=(748,664 ))],
    [sg.Column(layout2, background_color='#3CB371',size=(315,642 )), sg.Column(layout, background_color='#3CB371', size=(782,642 ))],


]

window = sg.Window("Sistema de envio Inteligênte de Whatsapp", layout_principal, icon='recursos/imagens/icone.ico', alpha_channel=0.9).Finalize()


while True:

    event, values = window.read()
    if event in (None, 'Close Window'):



        window.close()
        break


    arquivo_csv_dinamico = (values['file'])
    arquivo_excel_dinamico = (values['saida'])
    arquivo_foto_dinamico = (values['arquivo'])
    arquivo_legenda_dinamico = (values['legenda'])
    arquivo_replica_negativa_dinamico = (values['replica_negativa'])
    arquivo_resposta_cond1 = (values['resposta_cond_1'])
    arquivo_foto_dinamico_resposta = (values['foto_resposta'])
    arquivo_escuta_positiva = (values['escuta_positiva'])
    arquivo_escuta_negativa = (values['escuta_negativa'])
    valor_do_input = (values['input_excluir_individual'])
    arquivo_profile_n1 = (values['n1'])
    arquivo_profile_n2 = (values['n2'])
    arquivo_profile_n3 = (values['n3'])
    arquivo_profile_n4 = (values['n4'])
    arquivo_profile_n5 = (values['n5'])
    arquivo_profile_n6 = (values['n6'])
    arquivo_profile_n7 = (values['n7'])
    arquivo_profile_n8 = (values['n8'])
    arquivo_profile_n9 = (values['n9'])
    arquivo_profile_n10 = (values['n10'])

    numeros_de_telefone = [arquivo_profile_n1, arquivo_profile_n2, arquivo_profile_n3, arquivo_profile_n4,
                           arquivo_profile_n5, arquivo_profile_n6,
                           arquivo_profile_n7, arquivo_profile_n8, arquivo_profile_n9, arquivo_profile_n10]

    if event == 'iniciar':

        window.FindElement('iniciar').Update(disabled=True)
        window.FindElement('status').Update(text_color='#000000')
        window.FindElement('status').Update(background_color='#00FF00')
        window.FindElement('status').Update('RODANDO')

        lista_contatos = list(csv.reader(open(values['file']), delimiter=";"))
        numeros_de_telefone_para_enviar = ListaUtils.limpar_espacos_em_brancos(listao=numeros_de_telefone)


        lista_de_contato_para_enviar = ListaUtils.particionar_lista(lista_contatos, len(numeros_de_telefone_para_enviar))
        clientes_para_enviar = list(lista_de_contato_para_enviar)
        print('len', len(numeros_de_telefone_para_enviar))

        for numero_de_contato in numeros_de_telefone_para_enviar:
            print(f'Numero do telefone do profile -> {numero_de_contato}')
            print(f'Clientes para enviar -> {clientes_para_enviar}')
            for clientes in clientes_para_enviar:
                print(f'Cliente atual -> {clientes}')
                try:
                    Thread(target=send_msg_thread, args=(clientes, values['textbox'], values['response'], arquivo_foto_dinamico, arquivo_legenda_dinamico, numero_de_contato, window, ), daemon=True).start()
                    clientes_para_enviar.remove(clientes)
                except Exception as ex:
                    print(ex)
                    pass


    if event == 'configurar':
        if arquivo_profile_n1 == "":
                sg.Popup('Preencher o número do Profile')

        if arquivo_profile_n1 != "":
            Thread(target=configure_qrcode_thread, args=[numeros_de_telefone], daemon=True).start()


    if event == 'remover':

            excluindo_chave = deletar(chave=0)
            excluindo_chave.deletar_todos_os_profile()



    if event == 'responder':
        Thread(target=verify_msg_thread, args=(arquivo_csv_dinamico, arquivo_excel_dinamico, arquivo_foto_dinamico, arquivo_legenda_dinamico , arquivo_replica_negativa_dinamico, arquivo_resposta_cond1, arquivo_foto_dinamico_resposta, arquivo_escuta_positiva,  arquivo_escuta_negativa, numeros_de_telefone), daemon=True).start()
        window.FindElement('status').Update(text_color='#000000')
        window.FindElement('status').Update(background_color='#00FF00')
        window.FindElement('status').Update('RETORNO')

    if event == "Versão":
        sg.Popup("Whatsbot - Protótipo")

    if event == "Tutorial":

        os.startfile(dir_path + '\\recursos\\tutorial\\tutorialWhatsPrototipo.pdf')

    if event == "Sobre":
        sg.Popup("Somos a empresa Ok - Tecnologia, especializada em Softwares e Sites em geral. Contato: (Telefone da OK Tecnologia)")

    if event == 'botao_excluir_individual':
        excluindo_chave = deletar(chave=valor_do_input)
        excluindo_chave.delete()
        sg.Popup("Excluido")