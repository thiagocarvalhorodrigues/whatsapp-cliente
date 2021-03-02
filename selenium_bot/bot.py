import os.path
import time
import random
import urllib.parse
from tinydb import TinyDB, Query, where
from selenium import webdriver
import openpyxl
import csv
import pyautogui
from banco_profile.db import bancodedados
from logs.whats_log import funcao_warning
import PySimpleGUI as sg



###### INICIANDO O CHROMEDRIVER #######

class wppbot:


    dir_path = os.getcwd()

    def __init__(self,minimizer=True, file_csv=None, file_excel=None, file_foto=None, file_legenda=None, replica_negativa=None, resposta_cond1=None, file_foto_resposta=None,
                 file_escuta_positiva=None, file_escuta_negativa=None, numero_da_conta=None, sendmesenger=None):
        self.file_csv = file_csv
        self.file_excel = file_excel
        self.file_foto = file_foto
        self.file_legenda = file_legenda
        self.resposta_cond1 = resposta_cond1
        self.replica_negativa = replica_negativa
        self.file_foto_resposta = file_foto_resposta
        self.file_escuta_positiva = file_escuta_positiva
        self.file_escuta_negativa = file_escuta_negativa
        self.sendmesenger = sendmesenger
        self.numero_da_conta = numero_da_conta
        self.driver = self.configurar_driver(minimizer)
        # self.file_qrcode = file_qrcode
        # self.file_qrcode_range = self.file_qrcode


    def configurar_driver(self, minimizer=False,profile_id=0):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--silent ')
        self.options.add_argument('--log-level=3')
        self.options.add_argument('--lang=pt-BR')
        self.configurar_caminho_do_profile(profile_id)
        self.verificando_profile(profile_id)

        if minimizer == True:
            self.options.add_argument("--start-minimized")
            self.options.add_argument("--window-position=-10000,0")

        else:
            self.options.add_argument("--start-maximized")
            self.options.add_argument("--window-position=10,10")
            self.options.add_argument('--lang=pt-BR')





        return webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe',chrome_options=self.options)




    def configurar_caminho_do_profile(self,profile_id=0):
        db_profiles = bancodedados(numero_da_conta=self.getprofile(profile_id))

        resultado = db_profiles.encontrado()
        if self.getprofile(profile_id) != '':
               self.caminho = self.options.add_argument(r"--user-data-dir=" + self.dir_path + f'\profiles\{self.getprofile(profile_id)}\wpp')



        if self.getprofile(profile_id) == resultado:
            print(resultado,"resultado")

        else:

            print("Irá criar o Profile")
            if self.caminho == " ":
                print('vazio')
                return self.caminho


    def send_msg(self,site,template_response):
        db = TinyDB('db.json')


        self.driver.get(site)

        self.driver.execute_script("window.onbeforeunload = function() {};")
        time.sleep(15)


        botao_enviar = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
        botao_enviar.click()
        time.sleep(2)
        cell_number = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("title")
        db.insert({'num': cell_number, 'resp': urllib.parse.quote_plus(template_response)})
        time.sleep(5)

        # funcao_warning('FUNÇÃO SEND_MSG, Botão de enviar, local a onde pega o número do telefone do destinatário do chatbox')

        buttton_invalida_wpp = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
        if buttton_invalida_wpp.text == "OK":
            buttton_invalida_wpp.click()


        else:
            pass

              # funcao_warning('FUNÇÃO SEND_MSG, NÚMERO VÁLIDO NO WHATS ')


    def close_drive(self):
        self.driver.quit()


    ###### ABRE  O NAVEGADOR E LÊ O QRCODE #####
    def configure_qrcode(self):

        lista = self.numero_da_conta
        outraLista = [int(item) for item in lista if item.isdigit()]





        for nav in range(len(outraLista)):



            if nav > 0:


                self.driver = self.configurar_driver(profile_id=nav)



            self.driver.get('https://web.whatsapp.com/')




            qrcode_search = True
            while True:
                if qrcode_search is True:
                    try:
                        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas')
                        qrcode_search = False
                    except:
                        pass
                        # funcao_warning('Dentro da função configure_qrcode, XPATH do qrcode')
                        try:
                            self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
                            qrcode_search = False
                        except:
                            pass
                            # funcao_warning('Dentro da função configure_qrcode, não encontrou a FOTO DE PERFIL')
                else:
                    try:
                        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas')
                    except:
                        pass
                        # funcao_warning('Dentro da função configure_qrcode, XPATH do qrcode, dentro do ELSE')






                        while True:
                            try:
                                self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
                                time.sleep(1)
                                break
                            except:
                                pass
                                # funcao_warning('Dentro da função configure_qrcode no while True,  não encontrou a FOTO DE PERFIL')
                        break
            time.sleep(2)


            self.driver.close()
            self.driver.quit()
            nav += 1




    #### VERIFICA A RESPOSTA E CLICA NO ELEMENTO####
    def verify_msg_response(self):
        scroll_max = 0
        counter_scroll = 0



        self.driver.get('https://web.whatsapp.com/')


        time.sleep(5)
        self.driver.execute_script("window.onbeforeunload = function() {};")
        db = TinyDB('db.json')
        view = Query()

        while True:
            try:
                green_balls_notification = self.driver.find_elements_by_css_selector('span[class="_38M1B"]')


                if green_balls_notification == []:
                    if scroll_max == 0:
                        scroll_max = self.driver.execute_script('return document.querySelector("#pane-side").scrollHeight')
                    else:
                        counter_scroll += 1
                        self.driver.execute_script(f'document.querySelector("#pane-side").scrollTop = {counter_scroll}')




                else:

                    time.sleep(random.randrange(3,5,1)) ## TEMPO PARA CLICAR NA RESPOSTA
                    green_balls_notification[0].click()
                    self.sim_ou_nao()

                    person_cell_number = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("title")
                    json_db = db.search(view.num == person_cell_number)

                    if json_db:
                        number = json_db[0]['num'].replace(' ','').replace('-','').replace('+','')
                        msg = json_db[0]['resp']
                        print(f'{number} - Respondeu')
                        db.remove(where('num') == json_db[0]['num'])
                        self.driver.get(f'https://web.whatsapp.com/send?phone={number}&text={msg}')
                        time.sleep(5)

                        while True:
                            try:
                                botao_enviar = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                                botao_enviar.click()
                                time.sleep(2)

                                ##debugar##
                                if self.file_foto_resposta == "":
                                    pass
                                else:
                                    self.foto_resposta()
                                time.sleep(3)

                                self.driver.get('https://web.whatsapp.com/')



                                break
                            except:
                              pass


            except:
                pass

            if scroll_max < counter_scroll:
                counter_scroll = 0




    def escuta1(self):
        post = self.driver.find_elements_by_class_name('_1br5a')
        ultimo = len(post) - 1
        texto1 = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto1

    def escuta2(self):
        post = self.driver.find_elements_by_class_name('_1br5a')
        penultimo = len(post) - 2
        texto2 = post[penultimo].find_element_by_css_selector('span.selectable-text').text
        return texto2

    def escuta3(self):
        post = self.driver.find_elements_by_class_name('_1br5a')
        antipenultimo = len(post) - 3
        texto3 = post[antipenultimo].find_element_by_css_selector('span.selectable-text').text
        return texto3



    def entrando_lendo_csv(self):



        print("to dentro do CSV")

        arquivo = csv.reader(open(f'{self.file_csv}'), delimiter=';')


        self.contato = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("title")
        self.contatos_replace = self.contato.replace("+", "").replace(" ", "").replace("-", "")
        self.contatos_tudo_certo = self.contatos_replace
        self.novo_contato_tudo_certo = "9" + self.contatos_tudo_certo[4:]
        self.novo_contato_tudo_certo = (self.contatos_tudo_certo[0:4]) + self.novo_contato_tudo_certo
        self.dados = []

        for linha in arquivo:
            dados_linha = (linha[0], linha[1], linha[2], linha[3])
            if self.novo_contato_tudo_certo in dados_linha:
                self.dados.append(dados_linha)
                print("Adicionado Contato")




    def saindo_salvando_xlsx(self):
        print(self.file_excel)
        print("to_dentro_entrando_lendo_excel")
        print(f'{self.file_excel}')
        planilha = openpyxl.load_workbook(f'{self.file_excel}')
        print("dentro da planiha do excel")
        planilha_dado_completo = planilha['refin']
        planilha_dado_completo.append(self.dados[0])
        planilha.save(f'{self.file_excel}')
        print("Salvou no Excel")




    def sim_ou_nao(self):
        # self.respostas_positivas = (self.file_escuta_positiva)
        # self.respostas_negativas = (self.file_escuta_negativa)
        # print('Respostas negativas',self.respostas_negativas)
        # print('Respostas positivas', self.respostas_positivas)

        # if self.escuta1() in self.respostas_positivas or self.escuta2() in self.respostas_positivas or self.escuta3() in self.respostas_positivas:
        #     print("pegou do metodo SIM ---> POSITIVAS")

        time.sleep(2)
        print("resposta_cond1-->",self.resposta_cond1)
        if self.resposta_cond1 == "":
            print("resposta_cond1 dentro-->", self.resposta_cond1)
            pass
        else:
            caixa_mensagem = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            caixa_mensagem.send_keys(f'{self.resposta_cond1}')

        print('File CSV-->',self.file_csv)

        # # if self.file_csv == "":
        #     print('File CSV dentro -->', self.file_csv)
        #     pass
        # else:
        #     # self.entrando_lendo_csv()

        print('File EXCEL-->', self.file_excel)

        if self.file_excel == "":
            print('File EXCEL dentro -->', self.file_excel)
            pass

        else:
            self.saindo_salvando_xlsx()
            time.sleep(2)

        print("file_foto_resposta -->", self.file_foto_resposta)
        if self.file_foto_resposta == "":
            print("file_foto_resposta dentro -->", self.file_foto_resposta)
            pass
        else:
            self.foto_resposta()


        # if self.escuta1() in self.respostas_negativas or self.escuta2() in self.respostas_negativas or self.escuta3() in self.respostas_negativas:
        #     print("pegou do metodo SIM ---> NEGATIVAS")
        #     caixa_mensagem = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        #     caixa_mensagem.send_keys(f'{self.replica_negativa}')
        #     enviar = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        #     enviar.click()




    def foto(self):

        print("estou dentro do metodo da foto")

        clips = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        clips.click()
        time.sleep(3)
        foto = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        foto.click()
        time.sleep(5)
        caminho = (f'{self.file_foto}')
        caminho_ajustado = caminho.replace("/", "\\")
        time.sleep(5)
        pyautogui.typewrite(caminho_ajustado)
        time.sleep(5)
        pyautogui.press('tab', presses=2)
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(5)
        #legenda##
        legenda = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')
        legenda_mensagem = (f'{self.file_legenda}')
        time.sleep(10)
        legenda.send_keys(legenda_mensagem)
        time.sleep(10)
        enviar = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div')
        enviar.click()
        time.sleep(5)

    def foto_resposta(self):
        print("estou dentro do metodo da foto_resposta")
        clips = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        clips.click()
        time.sleep(5)
        foto = self.driver.find_element_by_xpath( '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        foto.click()
        time.sleep(5)
        caminho = (f'{self.file_foto_resposta}')
        caminho_ajustado = caminho.replace("/", "\\")
        time.sleep(5)
        pyautogui.typewrite(caminho_ajustado)
        time.sleep(5)
        pyautogui.press('tab', presses=2)
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(5)
        #legenda##
        legenda = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]')
        legenda_mensagem = (f'{self.file_legenda}')
        time.sleep(10)
        legenda.send_keys(legenda_mensagem)
        time.sleep(10)
        enviar = self.driver.find_element_by_xpath( '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div')
        enviar.click()
        time.sleep(2)

    def verificando_profile(self, profile_id=0):
        profile = bancodedados(numero_da_conta=self.getprofile(profile_id))
        profile.search_insert()

    def getprofile(self, profile_id=0):
        if self.sendmesenger is True:
            return self.numero_da_conta

        else:
            return self.numero_da_conta[profile_id]


