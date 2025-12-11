
class Configs:

    def __init__(self,largura,altura):

        self.largura = largura
        self.altura = altura
        self.cor_fundo = (50,50,50)

        # nave
        self.naveacel = 6

        #projetil
        self.velocidade_bala = 5
        self.largura_bala = 19 * 1 #se usar a forma do livro esse valor e 6
        self.nao_bala_atravessar = True #False ela atravessar
        self.altura_bala = 30 * 1 #se usar a forma do livro esse valor e 15
        self.cor_da_bala = (255, 0, 0)
        self.bala_permitidas = 3

        #alien
        self.vida_alien = 100
        self.velocidade_alien = 4
        self.temporario_alien = 4
        self.direcao = 1

        #velocidade do fundo
        self.velocidade_fundo=5

        self.selecao = False
        self.ajuda = False
        self.tela_inicio = True