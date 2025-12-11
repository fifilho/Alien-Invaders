import pygame as py
from pygame.sprite import Sprite
class Nave(Sprite):
    def __init__(self,configuracoes,tela,imagem):
        super(Nave,self).__init__()
        self.tela = tela
        self.image = imagem
        self.config = configuracoes
        #consiguir retangulos
        self.rect = self.image.get_rect()
        self.tela_retangulo = self.tela.get_rect()

        #vida nave
        self.vida = 3
        self.vida_total = 3
        self.dano = 100
        #colocar essas variaveis no negocio de status e mecher nelas na nave select por la tbm

        #centralizar
        self.rect.centerx = self.tela_retangulo.centerx
        self.rect.bottom = self.tela_retangulo.bottom

        #armazena o centro da nave em valores decimais
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.centery)

        # movimento
        self.andando_direita = False
        self.andando_esquerda = False
        self.subindo = False
        self.decendo = False

    def atualizar_nave(self):
        # ver se ta andando e colocar a posicao da nave de acordo e definir o limite da tela do lado esquerdo e direito
        if self.andando_direita and self.pos_x < self.tela_retangulo.right - 60:  # define o limite da tela do lado direito:
            self.pos_x += self.config.naveacel

        if self.andando_esquerda and self.pos_x > self.tela_retangulo.top - 60:  # define o limite da tela do lado esquerdo
            self.pos_x -= self.config.naveacel

        if self.subindo and self.pos_y > self.tela_retangulo.bottom - 200:
            self.pos_y -= self.config.naveacel

        if self.decendo and self.pos_y < self.tela_retangulo.bottom - 55:
            self.pos_y += self.config.naveacel

        self.rect.centerx = self.pos_x  # coloca o rentangulo como centro da nave
        self.rect.centery = self.pos_y

    def atualizar_jogo(self):
        self.atualizar_nave()

    def desenhar(self):
        self.tela.blit(self.image,self.rect)