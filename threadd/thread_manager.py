from selenium_bot.bot import wppbot
import urllib.parse
from utils.data_normalizer import fstr
import time
import random


##### JANELA QUE ENVIA AS MSGS #####

def send_msg_thread(lista_contatos, text_string, response, dinamico_foto, dinamico_legenda, window):
    bot = wppbot(minimizer=False, file_foto=dinamico_foto, file_legenda=dinamico_legenda)
    count = 1
    for coluna in lista_contatos:
        try:
            template_texto = fstr(text_string, coluna)
            template_response = fstr(response, coluna)
            time.sleep(random.randrange(5,10,1))
            bot.send_msg(f'https://web.whatsapp.com/send?phone={coluna[0]}&text={urllib.parse.quote_plus(template_texto)}',template_response)
            print(f'{str(count)} - {coluna[0]} - 1º contato')
            count +=1
            time.sleep(2)
            if bot.file_foto == "":
                pass
            else:
                bot.foto()
                time.sleep(20)


            bot.driver.get('https://web.whatsapp.com/')

        except:
            pass
    bot.close_drive()

    window.FindElement('status').Update(background_color='#FF0000')
    window.FindElement('status').Update('Finalizado')
    window.FindElement('iniciar').Update(disabled=False)



#####JANELA DA CONFIGURAÇÃO DO QRCODE #####
def configure_qrcode_thread(dinamico_qrcode):
    numero_da_conta = ("1234")
    bot = wppbot(minimizer=False, file_qrcode=dinamico_qrcode, numero_da_conta=numero_da_conta)
    bot.configure_qrcode()



###JANELA DE VERIFICAÇÃO DE MENSAGEM - RESPONDE###
def verify_msg_thread(dinamico_csv, dinamico_excel,dinamico_foto, dinamico_legenda, dinamico_replica_negativa, dinamico_resposta_cond1, dinamico_foto_resposta, dinamico_escuta_positiva,  dinamico_escuta_negativa):
    bot = wppbot(minimizer=False, file_csv=dinamico_csv, file_excel=dinamico_excel, file_foto=dinamico_foto, file_legenda=dinamico_legenda, replica_negativa=dinamico_replica_negativa, resposta_cond1=dinamico_resposta_cond1, file_foto_resposta=dinamico_foto_resposta, file_escuta_positiva=dinamico_escuta_positiva, file_escuta_negativa=dinamico_escuta_negativa)
    bot.verify_msg_response()









