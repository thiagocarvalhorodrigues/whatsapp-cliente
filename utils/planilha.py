# def verificar_chaves(self):
#     with open('C:\Desenvolvimento python\whats\recursos\dados_cliente.txt', 'r+') as arquivo:
#         lista = arquivo.read()
#         if self.caminho_total in lista:
#             print("tem chave")
#
#         else:
#             print("não tem chave")
#             print("salvando a chave")
#             arquivo.write(str(self.caminho_total) + '\n')

    # arquivo.close()

# class Planilha:




    # def lendo_valores_planilha(self):
    #     self.planilha = xlrd.open_workbook('gigante.xlsx')
    #     self.planilha_dado_completo = self.planilha.sheet_by_name('dados_completo')
    #     self.contato = ("+55 48 9193-8533")
    #
    #
    #     self.contatos_replace = self.contato.replace("+", "").replace(" ", "").replace("-", "")
    #
    #     self.contatos_tudo_certo = int(self.contatos_replace)
    #     print(self.contatos_tudo_certo)
    #     self.linha = self.planilha_dado_completo.nrows
    #     self.dados = []
    #     for i in range(self.linha):
    #         dados_linha = self.planilha_dado_completo.row_values(i)
    #         if self.contatos_tudo_certo in dados_linha:
    #             self.dados.append(dados_linha)
    #
    #
    # def pegando_valores_da_planilha_principal_e_salvando(self):
    #     planilha = openpyxl.load_workbook('Refin_corretor.xlsx')
    #     planilha_dado_completo = planilha['refin']
    #     valor = self.dados[0]
    #     planilha_dado_completo.append(valor)
    #     planilha.save('Refin_corretor.xlsx')



    # def pandas(self):
    #     #
    #     # dados = pd.read_csv('Refin_ENVIO.csv')
    #     # dados.head()
    #
    #     dados_selecionados = pd.read_csv('Refin_ENVIO.csv', usecols=[0])
    #     dados_selecionados.head()
    #     dados1 = dados_selecionados
    #     print(dados1)

# t = Planilha()
# t.lendo_valores_planilha()
# t.pegando_valores_da_planilha_principal_e_salvando()

# t = Planilha()
# t.pandas()

    # def entrando_lendo_csv(self):
    #     arquivo = csv.reader(open('Refin_ENVIO.csv'),delimiter=';')
    #     self.contato = ("+55 48 9193-8533")
    #     self.contatos_replace = self.contato.replace("+", "").replace(" ", "").replace("-", "")
    #     self.contatos_tudo_certo = self.contatos_replace
    #     self.novo_contato_tudo_certo = "9" + self.contatos_tudo_certo[4:]
    #     self.novo_contato_tudo_certo = (self.contatos_tudo_certo[0:4]) + self.novo_contato_tudo_certo
    #     print(self.novo_contato_tudo_certo)
    #     self.dados = []
    #
    #     for linha in arquivo:
    #         dados_linha = (linha[0], linha[1], linha[2], linha[3])
    #         if self.novo_contato_tudo_certo in dados_linha:
    #             self.dados.append(dados_linha)
    #             print(self.dados)
    #
#
# for linha in arquivo:
#     if not linha:
#         dados_linha = (linha[0], linha[1], linha[2], linha[3])
#         if self.novo_contato_tudo_certo in dados_linha:
#             self.dados.append(dados_linha)
#             print("Adicionado Contato")
#     #
    # def saindo_salvando_xlsx(self):
    #     planilha = openpyxl.load_workbook('Refin.xlsx')
    #     planilha_dado_completo = planilha['refin']
    #     planilha_dado_completo.append(self.dados[0])
    #     planilha.save('Refin.xlsx')



#
#
# t = Planilha()
# t.entrando_lendo_csv()
# t.saindo_salvando_xlsx()

###############FUNCIONANDO PARA EXCEL TOP#####################
# def escuta(self):
#     post = self.driver.find_elements_by_class_name('_1dB-m')
#     ultimo = len(post) - 1
#     texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
#     return texto
#
#
# def lendo_valores_planilha(self):
#     self.planilha = xlrd.open_workbook('Contatos.xlsx')
#     self.planilha_dado_completo = self.planilha.sheet_by_name('refin')
#     self.contato = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute(
#         "title")
#
#     self.contatos_replace = self.contato.replace("+", "").replace(" ", "").replace("-", "")
#
#     self.contatos_tudo_certo = int(self.contatos_replace)
#     self.linha = self.planilha_dado_completo.nrows
#     self.dados = []
#     for i in range(self.linha):
#         dados_linha = self.planilha_dado_completo.row_values(i)
#         if self.contatos_tudo_certo in dados_linha:
#             self.dados.append(dados_linha)
#
#
# def pegando_valores_da_planilha_principal_e_salvando(self):
#     planilha = openpyxl.load_workbook('Refin_corretor.xlsx')
#     planilha_dado_completo = planilha['refin']
#     valor = self.dados[0]
#     planilha_dado_completo.append(valor)
#     planilha.save('Refin_corretor.xlsx')






################ ESTAVA FUNCIONANDO NO CÓDIGO EXCEL PARA EXCEL #########################

# def lendo_valores_planilha(self):
#
#     self.planilha = xlrd.open_workbook('Contatos.xlsx')
#     self.planilha_dado_completo = self.planilha.sheet_by_name('refin')
#     self.contato = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("title")
#
#     self.contatos_replace = self.contato.replace("+", "").replace(" ", "").replace("-", "")
#
#     self.contatos_tudo_certo = int(self.contatos_replace)
#     self.linha = self.planilha_dado_completo.nrows
#     self.dados = []
#     for i in range(self.linha):
#         dados_linha = self.planilha_dado_completo.row_values(i)
#         if self.contatos_tudo_certo in dados_linha:
#             self.dados.append(dados_linha)

# def pegando_valores_da_planilha_principal_e_salvando(self):
#
#     planilha = openpyxl.load_workbook('Refin.xlsx')
#     planilha_dado_completo = planilha['refin']
#     valor = self.dados[0]
#     planilha_dado_completo.append(valor)
#     planilha.save('Refin.xlsx


# class arquivos:
#
#     def verificar_chaves(self, valor):
#         bot = wppbot(minimizer=True, file_chaves=valor)
#
#         print("entrando na verificação de chaves")
#         print(valor)
#         planilha = openpyxl.load_workbook('thiago.xlsx')
#         print("dentro verificar_chaves")
#         planilha_dado_completo = planilha['thiago']
#         print("dentro do workbook thiago")
#         planilha_dado_completo.append([valor])
#         planilha.save('thiago.xlsx')
#         print("final")
#
#
# rodar = arquivos()
# rodar.verificar_chaves("casa_top")








