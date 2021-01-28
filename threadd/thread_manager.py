from selenium_bot.bot import wppbot
import urllib.parse
from utils.data_normalizer import fstr
import time
import random


##### JANELA QUE ENVIA AS MSGS #####
from utils.lista_utils import ListaUtils
from utils.whatsapp_utils import WhatsappUtils


def send_msg_thread(lista_contatos, text_string, response, dinamico_foto, dinamico_legenda, numeros_de_telefone, window):

    [1, 2]

    # Pega o numero 1 e pega profile ->
    bot = wppbot(minimizer=False, file_foto=dinamico_foto, file_legenda=dinamico_legenda, numero_da_conta=numeros_de_telefone)

    lista_particionada = ListaUtils.particionar_lista(lista_contatos, 3)

    for list in lista_particionada:
        print(list)
        for contato in list:
            print(contato[0])
            enviar_mensagem(bot, contato, response, text_string)
            time.sleep(30)
        # Verificar o greenball
        wpp = WhatsappUtils(bot.driver)
        wpp.verify_msg_response()



    bot.close_drive()
    window.FindElement('status').Update(background_color='#FF0000')
    window.FindElement('status').Update('Finalizado')
    window.FindElement('iniciar').Update(disabled=False)


def enviar_mensagem(bot, numero_para_enviar_mensagem, response, text_string):

        try:
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



#####JANELA DA CONFIGURAÇÃO DO QRCODE #####
def configure_qrcode_thread(dinamico_qrcode,numeros_de_telefones):

    bot = wppbot(minimizer=False, file_qrcode=dinamico_qrcode, numero_da_conta=numeros_de_telefones)
    bot.configure_qrcode()



###JANELA DE VERIFICAÇÃO DE MENSAGEM - RESPONDE###
def verify_msg_thread(dinamico_csv, dinamico_excel,dinamico_foto, dinamico_legenda, dinamico_replica_negativa, dinamico_resposta_cond1, dinamico_foto_resposta, dinamico_escuta_positiva,  dinamico_escuta_negativa, numeros_de_telefones):
    bot = wppbot(minimizer=False, file_csv=dinamico_csv, file_excel=dinamico_excel, file_foto=dinamico_foto, file_legenda=dinamico_legenda, replica_negativa=dinamico_replica_negativa, resposta_cond1=dinamico_resposta_cond1, file_foto_resposta=dinamico_foto_resposta, file_escuta_positiva=dinamico_escuta_positiva, file_escuta_negativa=dinamico_escuta_negativa, numero_da_conta=numeros_de_telefones)
    bot.verify_msg_response()









