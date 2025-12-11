import pygame
from pygame.sprite import Sprite
from file_finder import resource_path
class Bala(Sprite):
    def __init__(self,configuracoes,tela,nave):
        super(Bala,self).__init__()

        self.tela = tela
        self.velocidade = configuracoes.velocidade_bala

        self.centro_bala = nave.rect.centerx
        self.topo_bala = nave.rect.top

        self.cor_bala = configuracoes.cor_da_bala


        self.image = pygame.image.load(resource_path('imagens_alien_invader/bala1.png'))
        self.image = pygame.transform.scale(self.image,(configuracoes.largura_bala,configuracoes.altura_bala))
        self.rect = self.image.get_rect()
        self.rect.centerx = nave.rect.centerx+1
        self.rect.top = nave.rect.top-11

        self.pos = float(self.rect.y)

    def update(self):
        """move o projetil"""
        #atualiza a posicao
        self.pos -= self.velocidade

        #atualiza a posicao tmb
        self.rect.y = self.pos

    #aprender o metodo do livro tbm mesmo ssendo mais "trabalhoso"