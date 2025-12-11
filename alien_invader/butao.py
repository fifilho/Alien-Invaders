import pygame as py
class BotaoJogar:
    def __init__(self,configuracoes,tela):
        self.configuracoes = configuracoes
        self.tela = tela
        self.tela_retangulo = tela.get_rect()

        self.largura, self.altura = 300*(self.tela.width/1200),100 *(self.tela.height/600)
        self.rect = py.Rect(0,0,self.largura, self.altura)
        self.rect.center = self.tela_retangulo.center
        self.rect.centerx = self.rect.centerx - self.tela_retangulo.width*0.003
        self.rect.centery = self.rect.centery + self.tela_retangulo.height*0.16
class BotaoNaves:
    def __init__(self,configuracoes,tela):
        self.configuracoes = configuracoes
        self.configuracoes = configuracoes
        self.tela = tela
        self.tela_retangulo = tela.get_rect()

        self.largura, self.altura = 300 * (self.tela.width / 1200), 100 * (self.tela.height / 600)
        # forma burra de fazer so pq eu ja tinha feito o botao na imagem em si a forma certta de fazer e isso ser a imagem tbm

        self.rect = py.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_retangulo.center
        self.rect.centerx = self.rect.centerx - self.tela_retangulo.width * 0.003
        self.rect.centery = self.rect.centery + self.tela_retangulo.height * 0.35
class BotaoAjudar:
    def __init__(self,configuracoes,tela):
        self.configuracoes = configuracoes
        self.tela = tela
        self.tela_retangulo = tela.get_rect()

        self.largura = 210 * (self.tela.width / 1200)  # 10 aproximadamente 1px
        self.altura = 85 * (self.tela.height / 600)  # 10 aproximadamente 1px
        self.rect = py.Rect(0, 0, self.largura, self.altura)
        self.rect.topright = (self.tela.width, 0)

class BotaoVoltar:
    def __init__(self,configuracoes,tela):
        self.configuracoes = configuracoes
        self.tela = tela
        self.tela_retangulo = tela.get_rect()


        self.largura = 210 * (self.tela.width/1200) #10 aproximadamente 1px
        self.altura = 85 * (self.tela.height / 600) #10 aproximadamente 1px
        self.rect = py.Rect(0, 0, self.largura, self.altura)
        self.rect.topright = (self.tela.width,0)
