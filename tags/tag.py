from enum import Enum


class Tag(Enum):
    BOTAO_ENVIAR = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]'
    TITULO_NUMERO_WHATS = 'title'
    ATIBUTO_DO_TITULO = '//*[@id="main"]/header/div[2]/div/div/span'
    BOTAO_INVALIDO = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
    BOTAO_DE_CONFIRMACAO_OK_DO_ELEMENTO_INVALIDO = 'OK'
    SITE = 'https://web.whatsapp.com/'
    QRCODE_SCANNER = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas'
    IMAGEM_PERFIL = '//*[@id="side"]/header/div[1]/div/img'
    JAVASCRIPT_ONEFORLOAD = 'window.onbeforeunload = function() {};'
    GREENBALL_ELEMENTO_PARA_RESPOSTA = 'span[class="_38M1B"]'
    TAG_SCROLL_MAX = 'return document.querySelector("#pane-side").scrollHeight'
    TAG_BOTAO_ENVIAR2 = '//*[@id="main"]/footer/div[1]/div[3]/button'
    IDENTIFICA_A_XPATH_DA_RESPOSTA = '_3ExzF'
    IDENTIFICA_O_TEXTO_DA_RESPOSTA = 'span.selectable-text'
    CAIXA_DE_MENSAGEM = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    CLIPS_BOTAO_PARA_ENVIAR_ANEXOS = '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span'
    FOTO_BOTAO_PARA_ANEXAR_FOTO = '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span'
    LEGENDA_CLICA_NO_XPATH = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]'
    LEGENDA_ENVIAR = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div'
    TAG_SCROOL_TOP = 'document.querySelector("#pane-side").scrollTop'
    BOTAO_TENTAR_NOVAMENTE = '//*[@id="app"]/div/div/div/div/div/div/div[3]/div[2]'
    TEXTO_TENTAR_NOVAMENTE = 'TENTAR NOVAMENTE'














