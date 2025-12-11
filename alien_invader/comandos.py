import sys
from tiro import Bala
from alien import Alien
import pygame as py
import json
from file_finder import resource_path
def checar_botao(status,botao_inicio,botao_ajuda,botao_nave,botao_voltar,mouse_x,mouse_y,configuracoes, tela, imagem, nave):
    if botao_inicio.rect.collidepoint(mouse_x, mouse_y) and configuracoes.tela_inicio == True:
        status.inicio = False
        configuracoes.tela_inicio = False
    elif botao_nave.rect.collidepoint(mouse_x, mouse_y) and configuracoes.tela_inicio == True:
        configuracoes.selecao = True
        configuracoes.tela_inicio = False
        tela_selecao(configuracoes, tela, imagem, nave,status,botao_inicio,botao_ajuda,botao_nave,botao_voltar)
    elif botao_voltar.rect.collidepoint(mouse_x, mouse_y) and configuracoes.selecao == True:
        configuracoes.selecao = False
        configuracoes.tela_inicio = True


def setar_status(nave,status):
    nave.vida = status["Vida"]
    nave.vida_total = status["Vida"]
    nave.dano = status["Dano"]

def stats_nave_atual(contador,nave):
    #os status sao organizados na seguinte ordem VIDA, DANO
    status_naves = {
        "nave_inicial":{"Vida":3, "Dano":100},
        "nave_rosa":{"Vida":5, "Dano":1000},
        "placeholder":{"Vida":"?", "Dano":"?"}
    }
    pont_max = pegar_pont_max()
    if contador == 1:
        status_display = status_naves["nave_inicial"]
        setar_status(nave,status_naves["nave_inicial"])
    elif contador == 2:
        if pont_max >10000:
            status_display = status_naves["nave_rosa"]
            setar_status(nave,status_naves["nave_rosa"])
        else:
            status_display = status_naves["placeholder"] #meh usei mal isso
            setar_status(nave, status_naves["nave_inicial"])
    else:
        #placeholder
        status_display = status_naves["placeholder"] #Ajeitar isso
        setar_status(nave,status_naves["nave_inicial"])

    return status_display

def nave_imagem(nave,contador):
    #pontuacao maxima
    pont_max = pegar_pont_max()
    # nave 1
    if contador == 1:
        nave.image = py.image.load(resource_path("imagens_alien_invader/nave.png"))

    # nave 2
    elif contador == 2:
        if pont_max >10000:
            nave.image = py.image.load(resource_path("imagens_alien_invader/nave_rosa.png"))
        else:
            nave.image = py.image.load(resource_path("imagens_alien_invader/nave.png"))
            return py.image.load(resource_path("imagens_alien_invader/nave_rosa.png"))#colocar imagem de nave com cadeado
    # Nave 3 (dourada mas por enquanto placeholder)
    elif contador == 3:
        # nave.image = py.image.load("imagens_alien_invader/nave_dourada.png")
        nave.image = py.image.load(resource_path("imagens_alien_invader/nave.png"))
        return py.image.load(resource_path("imagens_alien_invader/placeholder.png"))
    return nave.image

def tela_selecao(configuracoes,tela,imagem,nave,status,botao_inicial,botao_ajuda,botao_nave,botao_voltar):
    maquina = py.image.load(resource_path("imagens_alien_invader/tela_maquina.png"))
    maquina = py.transform.scale(maquina, (tela.get_width(), tela.get_height()))
    fonte_status = py.font.SysFont("Grand9K Pixel Regular", 60)
    while configuracoes.selecao:
        for evento in py.event.get():
            if evento.type == py.QUIT:
                sys.exit()
            elif evento.type == py.KEYDOWN:
                if evento.key == py.K_ESCAPE or evento.key == py.K_q:
                    if status.contador == 3:
                        status.contador = 1
                    configuracoes.selecao = False
                    configuracoes.tela_inicio = True
                if evento.key == py.K_RIGHT or evento.key == py.K_d:
                    status.contador += 1
                    if status.contador > 3:
                        status.contador = 1
                elif evento.key == py.K_LEFT or evento.key == py.K_a:
                    status.contador -= 1
                    if 1 > status.contador:
                        status.contador = 3
            elif evento.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                checar_botao(status,botao_inicial,botao_ajuda,botao_nave,botao_voltar,mouse_x,mouse_y,configuracoes, tela, imagem, nave)
        contador = status.contador
        enumeracao = 0
        nave_atual = nave_imagem(nave, contador)
        status_nave = stats_nave_atual(contador,nave)
        nave_atual = py.transform.scale(nave_atual, (220*(configuracoes.largura/1200), 220*(configuracoes.altura/600)))
        tela.blit(imagem, (0, 0))
        tela.blit(maquina, (0, 0))
        tela.blit(nave_atual, (configuracoes.largura*0.65, configuracoes.altura*0.4))

        for k,v in status_nave.items():
            nome = fonte_status.render(f"{k}:", False, (0, 0, 0))
            stat = fonte_status.render(f"{v}", False, (0, 0, 0))
            enumeracao += 1
            tela.blit(nome, (configuracoes.largura * 0.01,30+90*enumeracao))
            tela.blit(stat, (configuracoes.largura * 0.17, 30 + 90 * enumeracao))
        py.display.flip()

def tela_inicial(configuracoes,botao_inicial,botao_ajuda,botao_nave,botao_voltar,tela,imagem_inicial,fonte,status,imagem,nave):
      # se for colocar pra redimensionar a tela colocar a imagem dentro do loop e mudar a imagem final
    limite = py.time.Clock()
    # se for colocar pra redimensionar a tela colocar isso dentro do loop
    pontuacao_maxima = pontuacao_max(status)
    fase_max = fase_maxima(status)
    pont = fazer_o_texto(f"Best Score\n {pontuacao_maxima:>8}",fonte)
    fase = fazer_o_texto(f"Highest Level\n{fase_max:>13}", fonte)
    while status.inicio:
        tela.blit(imagem_inicial, (0, 0))
        tela.blit(pont, (configuracoes.largura*0.435, 0))
        tela.blit(fase, (configuracoes.largura*0.8, 0))
        py.display.flip()
        for evento in py.event.get():
            if evento.type == py.QUIT:
                sys.exit()
            elif evento.type == py.KEYDOWN:
                if evento.key == py.K_ESCAPE or evento.key == py.K_q:
                    sys.exit()
                elif evento.key == py.K_h:
                    ...
                    #tela_ajuda()
            elif evento.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                checar_botao(status, botao_inicial,botao_ajuda,botao_nave, botao_voltar, mouse_x, mouse_y, configuracoes, tela,imagem, nave)

        limite.tick(10)


def tela_final(configuracoes,tela,imagem_final,fundo_transparente,nave,tiros,background,aliens,status):
    limite = py.time.Clock()
    # se for colocar pra redimensionar a tela colocar a imagem dentro do loop e mudar a imagem final
    tela.blit(fundo_transparente, (0, 0))  # se for colocar pra redimensionar a tela colocar isso dentro do loop
    while not status.jogo_rodando:
        tela.blit(imagem_final, (0, 0))
        py.display.flip()
        checar_eventos(configuracoes,tela,nave,tiros,aliens,background,status)
        limite.tick(10)
def checar_eventos(configuracoes,tela,nave,tiros,aliens,background,status):
    """responde a esses checamentos abaixo"""
    for evento in py.event.get():
        if evento.type == py.QUIT:
            salvar_arquivos(status)
            sys.exit()
        elif evento.type == py.KEYDOWN:
            checar_presionamento_de_tecla(evento,configuracoes,tela,nave,tiros,aliens,background,status)

        elif evento.type == py.KEYUP:
            checar_levantamento_de_tecla(evento,nave)

def checar_presionamento_de_tecla(evento,configuracoes,tela,nave,tiros,aliens,background,status):
    """checa as teclas precisonadas"""
    if evento.key == py.K_d or evento.key == py.K_RIGHT:
        nave.andando_direita = True
    if evento.key == py.K_a or evento.key == py.K_LEFT:
        nave.andando_esquerda = True
    if evento.key == py.K_w or evento.key == py.K_UP:
        nave.subindo = True
    if evento.key == py.K_s or evento.key == py.K_DOWN:
        nave.decendo = True

    if evento.key == py.K_SPACE:
        atirar(configuracoes,tela,nave,tiros)

    if evento.key == py.K_ESCAPE:
        salvar_arquivos(status)
        sys.exit()
    elif evento.key == py.K_q:
        salvar_arquivos(status)
        configuracoes.tela_inicio = True
        resetar(configuracoes, tela, nave, tiros, aliens, background, status)
    elif evento.key == py.K_r:
        salvar_arquivos(status)
        resetar(configuracoes, tela, nave, tiros, aliens,background,status)

def checar_levantamento_de_tecla(evento,nave):
    """checa as teclas levantadas"""
    if evento.key == py.K_d or evento.key == py.K_RIGHT:
        nave.andando_direita = False
    if evento.key == py.K_a or evento.key == py.K_LEFT:
        nave.andando_esquerda = False

    if evento.key == py.K_w or evento.key == py.K_UP:
        nave.subindo = False
    if evento.key == py.K_s or evento.key == py.K_DOWN:
        nave.decendo = False

def atirar(configuracoes,tela,nave,tiros):
    """cria uma bala se n tiver demais"""
    if len(tiros) < configuracoes.bala_permitidas:
        bala_atual = Bala(configuracoes,tela,nave)
        tiros.add(bala_atual)

def update_balas(tiros):
    """atualiza as balas do tiro"""
    tiros.update()
    for bala in tiros.copy():
        if bala.rect.bottom <=0:
            bala.kill()

def consiguir_numero_de_aliens_lateral(configuracoes,largura_alien):
    espaco_disponivel_lateral = configuracoes.largura - (2 * largura_alien)
    numero_de_aliens = int(espaco_disponivel_lateral / (2 * largura_alien))
    return numero_de_aliens

def numero_de_linhas_para_aliens(configuracoes,alien,nave):
    espaco= configuracoes.altura-2*alien.rect.y-nave.rect.height #mudar para 3
    linhas= int(espaco / (2 * alien.rect.y))
    return linhas

def criar_alien(configuracoes,tela,aliens,numero_de_aliens,numero_linha):
    alien = Alien(configuracoes, tela)
    largura_alien = alien.rect.width
    alien.posicao_alien = (largura_alien + 2 * largura_alien * numero_de_aliens)
    alien.rect.x = alien.posicao_alien
    alien.rect.y = alien.rect.height +  2 * alien.rect.y * numero_linha
    aliens.add(alien)

def criar_frota(configuracoes,tela,aliens,nave):
    """cria a frota se a frota for menor que 4"""
    alien = Alien(configuracoes, tela)
    numero_de_aliens_lateral = consiguir_numero_de_aliens_lateral(configuracoes,alien.rect.width)
    linhas= numero_de_linhas_para_aliens(configuracoes,alien,nave)
    for linha_numero in range(linhas):
        for numero_de_aliens in range(numero_de_aliens_lateral):
            criar_alien(configuracoes,tela,aliens,numero_de_aliens,linha_numero)

def checar_borda(configuracoes,aliens):
    for alien in aliens.sprites():
        if alien.chechar_borda():
            mudar_direcao(configuracoes,aliens)
            break

def mudar_direcao(configuracoes,aliens):
    for alien in aliens.sprites():
        alien.rect.y += configuracoes.velocidade_alien
    configuracoes.direcao *= -1

def alien_no_fundo(configuracoes,tela,nave,tiros,aliens,background,status):
    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
            nave_recebeu_dano(configuracoes,tela,nave,tiros,aliens,background,status)
            break

def atualizar_aliens(configuracoes,tela,nave,tiros,aliens,background,status):
    checar_borda(configuracoes,aliens)
    aliens.update()
    alien_no_fundo(configuracoes,tela,nave,tiros,aliens,background,status)

def chechar_colisoes_aliens(configuracoes,tela,tiro,aliens,nave,status):
    #colisoes pelo visto checa as colisoes entre aliens e balas
    colisao = py.sprite.groupcollide(tiro,aliens,configuracoes.nao_bala_atravessar,False) #se o alien tiver mais que 1 de vida colocar uma variavel chamada colisoes aq
    if colisao:
        for alienigena in colisao.values():
            for alienigena_fudido in alienigena:
                Alien.update_vida(alienigena_fudido,nave,status)
    if len(aliens) == 0:
        passar_nivel(configuracoes,tela,tiro,aliens,nave,status)

def resetar_entidades(configuracoes,tela,tiros,aliens,nave):

    nave.pos_x = tela.get_rect().centerx
    nave.pos_y = tela.get_rect().bottom - 55
    nave.andando_direita = nave.andando_esquerda = nave.subindo = nave.decendo = False
    aliens.empty()
    tiros.empty()
    criar_frota(configuracoes, tela, aliens,nave)

def resetar(configuracoes,tela,nave,tiros,aliens,background,status):
    nave.vida = nave.vida_total
    background.velocidade = 0
    reset_game_state(status)
    resetar_entidades(configuracoes,tela,tiros,aliens,nave)


def reset_game_state(status):
    pontuacao_max(status)
    status.jogo_rodando = True
    status.inicio = True
    status.pontuacao_atual = 0
    status.nivel_atual = 1

def vida_nave(tela,nave,status):
    for c in range(1,nave.vida_total+1):
        tela.blit(status.imagem_coracao_perdido,(status.tamanho_coracao*c,0))
    for c in range(1,nave.vida+1):
        tela.blit(status.imagem_coracao,(status.tamanho_coracao*c,0))

def checar_dano_nave(configuracoes,tela,nave,tiros,aliens,background,status) :
    if py.sprite.spritecollideany(nave,aliens):
        nave_recebeu_dano(configuracoes, tela, nave, tiros, aliens, background,status)

def nave_recebeu_dano(configuracoes,tela,nave,tiros,aliens,background,status):
    aliens_atual = len(aliens)
    resetar_entidades(configuracoes, tela, tiros, aliens, nave)
    aliens_novos = len(aliens)
    background.velocidade = 0
    nave.vida -= 1
    status.pontuacao_atual -= (aliens_novos - aliens_atual) * 100
    if nave.vida <= 0:
        status.jogo_rodando = False

def passar_nivel(configuracoes,tela,tiros,aliens,nave,status):
    status.nivel_atual += 1
    if (status.nivel_atual % 10)==0:
        configuracoes.vida_alien *= 1.3
    aumentar_velocidade(configuracoes,status)
    resetar_entidades(configuracoes,tela,tiros,aliens,nave)


def aumentar_velocidade(configuracoes,status):
    if status.nivel_atual < 15:
        configuracoes.velocidade_alien *= 1.1
        configuracoes.temporario_alien *= 1.1
        configuracoes.velocidade_fundo *= 1.1

def desenhar(tela,nave,tiros,background,aliens,status):
    background.desenhar()
    nave.desenhar()
    tiros.draw(tela)
    aliens.draw(tela)
    vida_nave(tela, nave, status)

def desenhar_pontuacao(configuracoes,tela,status,fonte):
    mostrar_pontuacao(configuracoes, tela, status, fonte)
    mostrar_fase(configuracoes, tela, status, fonte)



def atualizar_tela(configuracoes,tela,nave,tiros,background,aliens,status,fonte):
    desenhar(tela,nave,tiros,background,aliens,status)
    desenhar_pontuacao(configuracoes,tela,status,fonte)
    py.display.flip()

def pegar_pont_max():
    try:
        with open("pontuacao_max.json" ,"r") as file:
            pontuacao_maxima = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pontuacao_maxima = 0
    return pontuacao_maxima

def pontuacao_max(status):
    try:
        with open("pontuacao_max.json" ,"r") as file:
            pontuacao_maxima = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pontuacao_maxima = 0
    if status.pontuacao_atual > pontuacao_maxima:
        with open("pontuacao_max.json","w") as file:
                json.dump(status.pontuacao_atual, file)
        return status.pontuacao_atual
    return pontuacao_maxima

def fase_atual(status):
    with open("Ultima_fase.json", "w") as f:
        json.dump(f"A fase mais atual que voce chegou foi a fase -> {status.nivel_atual}", f)

def fase_maxima(status):
    try:
        with open("fase_max.json", "r+") as file:
            fase_max = json.load(file)
    except FileNotFoundError:
        fase_max = 0
    if status.nivel_atual > fase_max:
        with open("fase_max.json", "w") as file:
            json.dump(status.nivel_atual, file)
        fase_max = status.nivel_atual
    return fase_max

def salvar_arquivos(status):
    fase_atual(status)
    fase_maxima(status)
    pontuacao_max(status)

def fazer_o_texto(texto_a_ser_feito,fonte):
    texto = fonte.render(str(texto_a_ser_feito), False, (255, 255, 255))
    return texto

def mostrar_pontuacao(configuracoes,tela,status,fonte):
    pontuacao = fazer_o_texto(status.pontuacao_atual,fonte)
    tela.blit(pontuacao, (int(configuracoes.largura / 2), 0))


def mostrar_fase(configuracoes,tela,status,fonte):
    fase = fazer_o_texto(f"Fase atual\n{status.nivel_atual:>9}",fonte)
    tela.blit(fase, (configuracoes.largura*0.85, 0))