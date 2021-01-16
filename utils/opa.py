import sys
import PySimpleGUI as sg


class popup:

    def thiaqo(self):

        sg.theme('TanBlue')
        background_fundo = '#FF4500'
        background_fonte = '#FFFAFA'

        popup = sg.popup("Números de Contas abertas: 255222",font=('Arial', 10, 'bold'), button_color=(background_fonte,background_fundo))
        if popup == "OK":
            sys.exit()





t = popup()
t.thiaqo()

#################################################
# sg.theme('Reddit')
# layout2 =   [
#             [sg.Text("Olá")],
#             [sg.Input(key='chave')],
#             [sg.Ok("OK")]
#             ]
# carro = sg.Window('janela', layout2).Finalize()
#
# while True:
#
#     evento, valores = carro.Read()
#     if evento == sg.WINDOW_CLOSED:
#         break
#     if evento == 'OK':
#         valor = valores["chave"]
#         print(valor)