import pygame
from pygame.sprite import Sprite
class Bala(Sprite):
    def __init__(self,  configuracoes, tela, nave):
        super().__init__()

        self.tela = tela
        self.image = pygame.Surface((configuracoes.largura_bala, configuracoes.altura_bala))
        self.image.fill(configuracoes.cor_da_bala)
        self.rect = self.image.get_rect()

        self.rect.centerx = nave.rect.centerx+1
        self.rect.y = nave.rect.top-11

        self.pos = float(self.rect.y)

        self.cor_bala = configuracoes.cor_da_bala
        self.velocidade = configuracoes.velocidade_bala

    def update(self):
        """move o projetil"""
        # atualiza a posicao
        self.pos -= self.velocidade

        # atualiza a posicao tmb
        self.rect.y = self.pos

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor_bala, self.rect)
        # aprender o metodo do livro tbm mesmo ssendo mais "trabalhoso"