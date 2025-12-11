import pygame as py
from file_finder import resource_path
class Status:
    def __init__(self):
        self.jogo_rodando = True
        self.inicio = True
        self.tamanho_coracao = 30

        self.imagem_coracao = py.image.load(resource_path("imagens_alien_invader/coracao.png"))
        self.imagem_coracao = py.transform.scale(self.imagem_coracao, (self.tamanho_coracao, self.tamanho_coracao))

        self.imagem_coracao_perdido = py.image.load(resource_path("imagens_alien_invader/coracao_machucado.png"))
        self.imagem_coracao_perdido = py.transform.scale(self.imagem_coracao_perdido, (self.tamanho_coracao, self.tamanho_coracao))

        self.nivel_atual = 1
        self.contador = 1
        self.pontuacao_atual = 0