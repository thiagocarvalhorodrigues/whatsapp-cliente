from selenium_bot.bot import wppbot
import urllib.parse
from utils.data_normalizer import fstr
import time
import random
from utils.lista_utils import ListaUtils
from utils.whatsapp_utils import WhatsappUtils
from banco_enviar_quantidade_de_contatos.db_envio_contatos import banco_envio_contatos
from logs.whats_log import funcao_warning



################## -- THREADS -- ####################
def  send_msg_thread(contatos, text_string, response, dinamico_foto, dinamico_legenda, numeros_de_telefone, window):
    bot = wppbot(minimizer=False, file_foto=dinamico_foto, file_legenda=dinamico_legenda,numero_da_conta=numeros_de_telefone, sendmesenger=True)
    print('NÚMERO DO PROFILE-->',numeros_de_telefone)

    select_no_banco_qtd_envio_de_contatos  = banco_envio_contatos(quantidade_contato=0)
    qtd_envio_de_contatos = select_no_banco_qtd_envio_de_contatos.select_all()
    qtd_envio_de_contatos_a_enviar = int(qtd_envio_de_contatos[0]['contato'])
    print('quantidade_de_contatos_a_enviar', qtd_envio_de_contatos_a_enviar)



    lista_de_contatos = ListaUtils.particionar_lista(contatos,qtd_envio_de_contatos_a_enviar)

    for clientes in lista_de_contatos:
        print('CLIENTES-->', clientes)

        for contato in clientes:

            enviar_mensagem(bot, contato, response, text_string)
            time.sleep(30)
        # Verificar o greenball
        wpp = WhatsappUtils(bot.driver)
        wpp.verify_msg_response()
        time.sleep(120)


    bot.close_drive()
    window.FindElement('status').Update(background_color='#FF0000')
    window.FindElement('status').Update('Finalizado')
    window.FindElement('iniciar').Update(disabled=False)


def enviar_mensagem(bot, numero_para_enviar_mensagem, response, text_string):

        try:
            print('numero_para_enviar_mensagem -->', numero_para_enviar_mensagem)
            template_texto = fstr(text_string, numero_para_enviar_mensagem)
            template_response = fstr(response, numero_para_enviar_mensagem)
            time.sleep(random.randrange(5, 10, 1))
            bot.send_msg( f'https://web.whatsapp.com/send?phone={numero_para_enviar_mensagem[0]}&text={urllib.parse.quote_plus(template_texto)}',template_response)
            print(f' {numero_para_enviar_mensagem[0]} - 1º contato')
            time.sleep(2)  ## tempo de esperar para enviar a mensagem para outro cliente.
            if bot.file_foto == "":
                pass
            else:
                bot.foto()
                time.sleep(20)

            bot.driver.get('https://web.whatsapp.com/')

        except:
            pass
            # funcao_warning('DENTRO DA FUNÇÃO enviar_mensagem, algum problema ao enviar mensagem e/ou arquivo de foto')



#####JANELA DA CONFIGURAÇÃO DO QRCODE #####
def configure_qrcode_thread(numeros_de_telefones):

    bot = wppbot(minimizer=False, numero_da_conta=numeros_de_telefones)
    bot.configure_qrcode()



###JANELA DE VERIFICAÇÃO DE MENSAGEM - RESPONDE###
def verify_msg_thread(dinamico_csv, dinamico_excel,dinamico_foto, dinamico_legenda, dinamico_replica_negativa, dinamico_resposta_cond1, dinamico_foto_resposta, dinamico_escuta_positiva,  dinamico_escuta_negativa, numeros_de_telefones):
    bot = wppbot(minimizer=False, file_csv=dinamico_csv, file_excel=dinamico_excel, file_foto=dinamico_foto, file_legenda=dinamico_legenda, replica_negativa=dinamico_replica_negativa, resposta_cond1=dinamico_resposta_cond1, file_foto_resposta=dinamico_foto_resposta, file_escuta_positiva=dinamico_escuta_positiva, file_escuta_negativa=dinamico_escuta_negativa, numero_da_conta=numeros_de_telefones)
    bot.verify_msg_response()