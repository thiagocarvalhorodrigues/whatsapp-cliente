import PySimpleGUI as sg
import csv
from threadd.thread_manager import send_msg_thread, configure_qrcode_thread, verify_msg_thread
from threading import Thread
from banco_profile import db
import shutil
from banco_profile.deletando import deletar
# import pygame
# pygame.init()
# pygame.mixer.music.load("musica.ogg")
# pygame.mixer.music.play()
# pygame.event.wait()

sg.theme('TanBlue')
background_fundo = '#FF4500'
background_fonte = '#FFFAFA'


menu_tela_inicial = [
    ['Ajuda',[ 'Versão']],
    ['Contato',['Sobre']]

    ]


layout =    [[sg.Image('recursos/imagens/Logo700x100.png')],
            [sg.Menu(menu_tela_inicial)],
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


global valor_do_input
dados = db.bancodedados(numero_da_conta='0')
(select_dos_numeros_cadastrados) = (dados.select_all())
print(select_dos_numeros_cadastrados)


layout2 = [[sg.Image('recursos/imagens/convertido.png')],
        [sg.Text('Quantas contas desejar Abrir?', text_color=background_fonte,background_color='#3CB371', font=('Arial', 10, 'bold'))],
        [sg.Slider(range=(1,10),default_value=1, background_color=background_fonte, text_color='#3CB371' ,orientation='h', key='qrcode')],
        [sg.Text("Informe os números que deseja enviar as mensagens", text_color=background_fonte, background_color='#3CB371', font=('Arial',10, 'bold'))],
        [sg.Text("1º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[0]['celular'], key="n1",size=(13,1))],
        [sg.Text("2º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[1]['celular'], key="n2",size=(13, 1))],
        [sg.Text("3º Número",text_color=background_fonte,  background_color='#3CB371', font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[2]['celular'],key="n3",size=(13, 1))],
        [sg.Text("4º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[3]['celular'],key="n4",size=(13, 1))],
        [sg.Text("5º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12)),sg.Text("          ", background_color='#3CB371'), sg.Button('Excluir QRCode Indivídual',button_color=(background_fonte,background_fundo), key='botao_excluir_individual')],
        [sg.Input(select_dos_numeros_cadastrados[4]['celular'],key="n5",size=(13, 1)),sg.Text("                ", background_color='#3CB371'),  sg.Input(key="input_excluir_individual",size=(10,1))],
        [sg.Text("6º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12)), sg.Text("                         ex: n1 - n2",text_color=background_fonte,background_color='#3CB371')],
        [sg.Input(select_dos_numeros_cadastrados[5]['celular'],key="n6",size=(13, 1))],
        [sg.Text("7º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[6]['celular'],key="n7",size=(13, 1))],
        [sg.Text("8º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[7]['celular'],key="n8",size=(13, 1))],
        [sg.Text("9º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[8]['celular'],key="n9",size=(13, 1))],
        [sg.Text("10º Número",text_color=background_fonte, background_color='#3CB371',font=('Arial',12))],
        [sg.Input(select_dos_numeros_cadastrados[9]['celular'],key="n10",size=(13, 1))]




    ]



layout3 = [
    [sg.Text('Enviar SPAM?                                      Preencher SAUDAÇÃO e RESPOSTA.', background_color='#34af23')],
    [sg.Text('Perguntar direto na SAUDAÇÃO?           Prenncher SAUDAÇÃO e RESPOSTA CONDICIONAL 1.', background_color='#34af23')],
    [sg.Text('Perguntar direto na RESPOSTA?           Preenchar SAUDAÇÃO, RESPOSTA e RESPOSTA CONDICIONAL 1. ', background_color='#34af23')],




]





layout_principal = [

    [sg.Frame("Configurações de envio de mensagens",layout2, background_color='#3CB371',border_width='3px', title_color='#000000'),sg.Frame('Acões',layout, background_color='#3CB371', border_width='3px', title_color='#000000')],
    [sg.Text("                                                        "),sg.Frame("Tutorial",layout3, element_justification="center", background_color='#3CB371', border_width='3px', title_color='#000000')],



]


window = sg.Window("Whatsapp", layout_principal, alpha_channel=0.9).Finalize()




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
    arquivo_qrcode = int((values['qrcode']))
    arquivo_profile_n1 = (values['n1'])
    valor_do_input = (values['input_excluir_individual'])




    if event == 'iniciar':

        window.FindElement('iniciar').Update(disabled=True)
        window.FindElement('status').Update(text_color='#000000')
        window.FindElement('status').Update(background_color='#00FF00')
        window.FindElement('status').Update('RODANDO')
        lista_contatos = list(csv.reader(open(values['file']), delimiter=";"))

        Thread(target=send_msg_thread, args=(lista_contatos, values['textbox'], values['response'], arquivo_foto_dinamico, arquivo_legenda_dinamico, window, ), daemon=True).start()

    if event == 'configurar':
        Thread(target=configure_qrcode_thread, args=[arquivo_qrcode, arquivo_profile_n1], daemon=True).start()


    if event == 'remover':
        try:
            shutil.rmtree('profiles', ignore_errors=False, onerror=None)
        except:
            pass
    if event == 'responder':
        Thread(target=verify_msg_thread, args=(arquivo_csv_dinamico, arquivo_excel_dinamico, arquivo_foto_dinamico, arquivo_legenda_dinamico , arquivo_replica_negativa_dinamico, arquivo_resposta_cond1, arquivo_foto_dinamico_resposta, arquivo_escuta_positiva,  arquivo_escuta_negativa), daemon=True).start()
        window.FindElement('status').Update(text_color='#000000')
        window.FindElement('status').Update(background_color='#00FF00')
        window.FindElement('status').Update('RETORNO')

    if event == "Versão":
        sg.Popup("Whatsbot - Protótipo")

    if event == "Sobre":
        sg.Popup("Somos a empresa Ok - Tecnologia, especializada em Softwares e Sites em geral. Contato: (Telefone da OK Tecnologia)")

    if event == 'botao_excluir_individual':
        excluindo_chave = deletar(chave=valor_do_input)
        excluindo_chave.delete()
        sg.Popup("Excluido")

    if event == "Excluido":
        print("Coisa linda")
