from nave import Nave
import pygame as py
import comandos
from status import Status
from config import Configs
from butao import BotaoJogar,BotaoNaves,BotaoVoltar,BotaoAjudar
from pygame.sprite import Group
from background import Background
from file_finder import resource_path
n_escolha = True
while n_escolha:
    print(f"{'Escolha a resolução':>30}")
    print("1 - 1280 × 720")
    print("2 - 1366 × 768")
    print("3 - 1600 × 900")
    print("4 - 1920 × 1080")
    dec = input("> ")

    if dec == "1":
        largura, altura = 1280, 720
        n_escolha = False
    elif dec == "2":
        largura, altura = 1366, 768
        n_escolha = False
    elif dec == "3":
        largura, altura = 1600, 900
        n_escolha = False
    elif dec == "4":
        largura, altura = 1920, 1080
        n_escolha = False
    else:
        print("Escolha uma opção válida!")
def rodar_jogo():
    """roda o jogo"""
    py.init()  # inicia o jogo

    #colocar a vida no canto esquerdo em cima

    configuracoes= Configs(largura,altura)

    tela = py.display.set_mode((configuracoes.largura, configuracoes.altura))#resolucao tela

    imagem_nave = py.image.load(resource_path("imagens_alien_invader/nave.png"))

    nave : Nave  = Nave(configuracoes,tela,imagem_nave)# a nave

    tickrate = py.time.Clock()

    botao_inicial = BotaoJogar(configuracoes,tela)
    botao_nave = BotaoNaves(configuracoes,tela)
    botao_voltar = BotaoVoltar(configuracoes,tela)
    botao_ajuda = BotaoAjudar(configuracoes,tela)

    status = Status()

    tiros = Group()

    aliens = Group()#o alien

    imagem_inicial = py.image.load(resource_path("imagens_alien_invader/Tela_inicial.png"))
    imagem_inicial = py.transform.scale(imagem_inicial, (tela.get_width(), tela.get_height()))

    imagem_final = py.image.load(resource_path("imagens_alien_invader/Imagem_Final.png"))
    imagem_final = py.transform.scale(imagem_final, (tela.get_width(), tela.get_height()))

    fundo = py.image.load(resource_path("imagens_alien_invader/fundoinc.png"))
    fundo = py.transform.scale(fundo, (configuracoes.largura, configuracoes.altura))

    fundo_transparente = py.image.load(resource_path("imagens_alien_invader/Fundo_Transparente.png"))
    fundo_transparente = py.transform.scale(fundo_transparente, (tela.get_width(), tela.get_height()))

    fonte = py.font.SysFont("Grand9K Pixel Regular", 30)

    background = Background(configuracoes, tela, fundo, nave)

    py.display.set_caption('Projeto Tyrone') # coloca o nome em cima

    comandos.criar_frota(configuracoes, tela, aliens,nave)
    # meio obvio mas cria uma frota de aliens

    while status.jogo_rodando:

        #colocar tudo aqui em uma game func talvez

        comandos.checar_eventos(configuracoes,tela,nave,tiros,aliens,background,status)
        #checa se clicou algo
        #e manda esse comando para atirar ou sair do jogo ou mover a nave

        nave.atualizar_jogo()
        #atualiza as posicoes da nave de acordo com a funcao acima


        tiros.update()
        #atualiza as posicoes do tiro diminuindo o valor para ir pra cima

        comandos.atualizar_aliens(configuracoes,tela,nave,tiros,aliens,background,status)

        comandos.chechar_colisoes_aliens(configuracoes,tela,tiros,aliens,nave,status)
        #checa se um tiro colidiu
        # e em seguida reduz a vida em 1 se chegar em 0 o alien morre
        comandos.checar_dano_nave(configuracoes,tela,nave,tiros,aliens,background,status)

        comandos.update_balas(tiros)

        comandos.atualizar_tela(configuracoes,tela,nave,tiros,background,aliens,status,fonte)
        #mostra essas posicoes e da ""refresh na tela""
        # esse refresh acima na real ele apaga a tela e reescreve dando sensacao de fluidez

        tickrate.tick(60) # deixa fixo o fps
        if not status.jogo_rodando:
            comandos.tela_final(configuracoes,tela,imagem_final,fundo_transparente,nave,tiros,background,aliens,status)
            comandos.resetar(configuracoes,tela,nave,tiros,aliens,background,status)
        elif status.inicio:
            comandos.atualizar_tela(configuracoes,tela,nave,tiros,background,aliens,status,fonte)
            comandos.tela_inicial(configuracoes,botao_inicial,botao_ajuda,botao_nave,botao_voltar,tela,imagem_inicial,fonte,status,fundo,nave)
rodar_jogo()