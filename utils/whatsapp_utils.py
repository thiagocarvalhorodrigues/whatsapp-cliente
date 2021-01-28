from tinydb import TinyDB, Query, where
import time
import random


class WhatsappUtils:

    def __init__(self,driver):
        self.driver =driver

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
                green_balls_notification = self.driver.find_elements_by_css_selector('div[class="_2Q3SY"]')

                if green_balls_notification == []:
                    if scroll_max == 0:
                        scroll_max = self.driver.execute_script(
                            'return document.querySelector("#pane-side").scrollHeight')
                    else:
                        counter_scroll += 1
                        self.driver.execute_script(f'document.querySelector("#pane-side").scrollTop = {counter_scroll}')




                else:

                    time.sleep(random.randrange(3, 5, 1))  ## TEMPO PARA CLICAR NA RESPOSTA
                    green_balls_notification[0].click()

                    # self.sim_ou_nao()

                    person_cell_number = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("title")

                    json_db = db.search(view.num == person_cell_number)

                    if json_db:
                        number = json_db[0]['num'].replace(' ', '').replace('-', '').replace('+', '')
                        msg = json_db[0]['resp']
                        print(f'{number} - Respondeu')
                        db.remove(where('num') == json_db[0]['num'])
                        self.driver.get(f'https://web.whatsapp.com/send?phone={number}&text={msg}')
                        time.sleep(5)
                        while True:
                            try:
                                botao_enviar = self.driver.find_element_by_xpath( '//*[@id="main"]/footer/div[1]/div[3]/button')
                                botao_enviar.click()
                                time.sleep(2)
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
