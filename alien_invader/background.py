from math import ceil
class Background:
    def __init__(self, configuracoes, tela,backgrounde,nave):
        self.configuracoes = configuracoes
        self.tela = tela
        self.backgrounde = backgrounde
        self.background_altura = self.backgrounde.get_height()
        self.tela_altura = self.tela.get_height()
        self.quadradinhos = ceil(self.tela_altura / self.background_altura)+1
        self.velocidade = 0
        self.nave = nave

    def desenhar(self):

        for c in range(-1, self.quadradinhos ):
            pos=c * self.background_altura + self.velocidade
            self.tela.blit(self.backgrounde,(0,pos))

        if self.nave.subindo or self.nave.pos_y < self.background_altura-100:
            self.velocidade += self.configuracoes.velocidade_fundo * 2
            self.configuracoes.velocidade_alien = self.configuracoes.temporario_alien * 2
        else:
            self.velocidade += self.configuracoes.velocidade_fundo
            self.configuracoes.velocidade_alien = self.configuracoes.temporario_alien
        if self.velocidade >= self.background_altura:
                self.velocidade = 0