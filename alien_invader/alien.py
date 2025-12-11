import pygame
from pygame.sprite import Sprite
from file_finder import resource_path

class Alien(Sprite):
    def __init__(self,configuracoes,tela):
        super().__init__()
        self.tela = tela
        self.configuracoes = configuracoes


        self.image = pygame.image.load(resource_path('imagens_alien_invader/nave1.png')).convert_alpha()
        self.rect= self.image.get_rect()

        self.vida = self.configuracoes.vida_alien

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.posicao_alien= float(self.rect.x)

    def chechar_borda(self):
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def update(self):
        self.posicao_alien += self.configuracoes.velocidade_alien * self.configuracoes.direcao
        self.rect.x = self.posicao_alien

    def update_vida(self,nave,status):
        if (self.vida - nave.dano)<=0:
            self.kill()
            status.pontuacao_atual += 100
        else:
            self.vida -= nave.dano