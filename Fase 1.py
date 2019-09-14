import pygame, sys, random      #Biblioteca usada na criação de aplicações multimídia
from pygame.locals import *     #Várias constantes usadas pelo pygame


# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------

pygame.init()                   # Inicialisa todos o módulos importados do pygame
Relogio = pygame.time.Clock()   # Cria um objeto pra ajudar a rastrear o tempo
LARGURA = 1020                  # Largura da tela
ALTURA = 600                    # Altura da tela
Janela = pygame.display.set_mode((LARGURA, ALTURA)) # Inicializa uma tela para exibit
pygame.display.set_caption('Fase 1')                # Coloca um título para a tela
QPS=120                         # Quadros por segundo
Ligado = X = Y = Acertou = chao = False          # Variáveis de controle
texto=''                        # Vamos usar pra caixa de texto
f=100                             # Fator de escala (f pixel/m)
g=f*9.81                        # Gravidade (convertida para pixel / s²)
dT=0.2/f                        # Intervalo dos passos (m*s/pixel*quadro)

# Algumas cores
PRETO  = (0, 0, 0)
CINZA = (200,200,200)
VERDE  = (0, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255,0,0)

# Uma fonte
FONTE = pygame.font.Font('freesansbold.ttf', 32)    #Cria um objeto de fonte
FIMFONTE = pygame.font.Font('freesansbold.ttf', 100)

# Estruturas
Estruturas = []
e = 10                                                      # Espessura
# pygame (esquerda, topo, largura, altura) -> Objeto para guardar coordenadas retangulares
Estruturas.append(pygame.Rect(0, ALTURA-e, LARGURA, e))     # Chão
Estruturas.append(pygame.Rect(LARGURA-e, 0, e, ALTURA))     # Parede direita
Estruturas.append(pygame.Rect(LARGURA-300, ALTURA*(1-1/3), e, ALTURA/3))     #Parede do meio

#Alvo
alvo=pygame.Rect(155-10, 590-20, 20, 20)

#Vamos definir nosso projétil
class Projetil:                 # A classe projetil
    def __init__(self):
        self.vx = 0             # Sua velocidade no eixo x (em pixel/s)
        self.vy = 0             # Sua velocidade no eixo y (em pixel/s)
        self.pos = (755,580)    # Sua localização
        self.raio = 5           # Seu raio
        
p = Projetil()                  # Declaramos o objeto

#Vamos definir os textos
#font.render (texto, atialias, cor, fundo=None)     -> desenha um texto em uma superficie
simtexto = (FONTE.render('Simular', True, BRANCO, PRETO))
reitexto = (FONTE.render('Reiniciar', True, BRANCO, PRETO))
vxtexto = (FONTE.render("Vx: {:10.2f}".format(p.vx/f), True, PRETO))
vytexto = (FONTE.render("Vy: {:10.2f}".format(p.vy/f), True, PRETO))


#Áreas clicaveis
simret = simtexto.get_rect()   #Pega as informações da área retangular
simret.center = (100, 50)      #Definimo o centro do texto
reiret = reitexto.get_rect()   
reiret.center = (300, 50)
vxret = vxtexto.get_rect()   
vxret.center = (100, 100)
vyret = vytexto.get_rect()   
vyret.center = (100, 150)


# 2 - ENTRADAS ------------------------------------------------------------------------------
while True:
    # Vamos checar por eventos
    for evento in pygame.event.get():       # Pega eventos da fila
        if evento.type == QUIT:             # Se tentou fechar o jogo
            pygame.quit()                   # Fecha todos os módulos
            sys.exit()                      # Sai do Python
        if evento.type == MOUSEBUTTONUP:    # Se clicou
            #Vamos verificar se clicou em algum botão
            if (simret.collidepoint(evento.pos[0],evento.pos[1]) and X==Y==False):  # Botão de simular
                Ligado=True
            elif reiret.collidepoint(evento.pos[0],evento.pos[1]):                  # Botão de reiniciar
                p= Projetil()
                Ligado = X = Y = Acertou = chao = False
            elif (vxret.collidepoint(evento.pos[0],evento.pos[1])):                 # Ajustar velocidade no eixo X
                  if (Ligado == False and Y==False):
                      X=True
            elif (vyret.collidepoint(evento.pos[0],evento.pos[1])):                 #Ajustar velocidade no eixo Y
                  if (Ligado == False and X==False):
                      Y=True
        if evento.type == KEYDOWN:                          # Se pressionou algum botão
            if (Ligado == False and X==True and Y==False):  # E estamos editando Vx
                if evento.key == K_RETURN:                  # Enter
                    p.vx=abs(float(texto))*f
                    texto=""
                    X=False
                elif evento.key == K_BACKSPACE:             # Backspace 
                    texto=texto[:-1]
                else:
                    texto += evento.unicode                 # Dígito qualquer
                    
            elif (Ligado == False and Y==True and X==False):# Se estamos editando Vy
                if evento.key == K_RETURN:
                    p.vy=float(texto)*f
                    texto=""
                    Y=False
                elif evento.key == K_BACKSPACE:
                    texto=texto[:-1]
                else:
                    texto += evento.unicode
                
# 3 - Motor de Física ---------------------------------------------------------------------------

    if (Ligado):

        #3.1 Horizontal #############################################################################

        p.pos = ((p.pos[0]+p.vx*dT),p.pos[1])           # MRU
        
        # Vamos testar se o projétil colidou com alguma estrutura
        n=0     #contador
        for est in Estruturas:
            if(est.collidepoint(p.pos) and p.pos[1]<ALTURA-e):                # Testamos se o rect est colidiu com o ponto p.pos
                if (n!=0):                                  #Ignoramos colisão com o chão
                    p.vx=-p.vx                              # Invertemos a velocidade
                    if (n==1):                              # Colisão com a parede da direita
                        dx=p.pos[0]-1010
                        p.pos = (1010-dx,p.pos[1]) # Corrigmos o deslocamento
                    if (n==2):                              # Colisão com a parede do meio
                        dx=730-p.pos[0]
                        p.pos = (730+dx,p.pos[1]) # Corrigmos o deslocamento
            n=n+1
        
        # 3.2 Vertical ################################################################################

        if (chao==False):                                   # Se não atingiu o chão
            p.pos = (p.pos[0], p.pos[1]-p.vy*dT-g*(dT*dT)/2)# MRUV
            p.vy=p.vy-g*dT                                  # Ajustamos a velocidade

    
        if(Estruturas[0].collidepoint(p.pos)):                    # Deixamos no chão
            p.vy=0
            p.vx=0
            p.pos = (p.pos[0],ALTURA-e)
            chao=True

        # 3.3 Colisão com alvo ########################################################################
        if (alvo.collidepoint(p.pos)):
            Acertou=True


# 4 - Atualização da Tela ----------------------------------------------------------------------

    # Pinta o fundo
    Janela.fill(BRANCO)             # Preenche a superfície com uma cor sólida

    #Pinta os textos:
    Janela.blit(simtexto, simret)   # Desenha um imagem em outra (Fonte, destino)
    Janela.blit(reitexto, reiret)

    if (Acertou==False):            # Se não acertou
        #Atualiza as velocidades na tela
        if (X == False):            # Se não estamos editando Vx
            vxtexto = (FONTE.render("Vx: {:10.2f}".format(p.vx/f), True, PRETO))
        else:                       # Se estamos editando Vx
            vxtexto = FONTE.render(texto, True, CINZA)
        if (Y == False):            # O mesmo para Vy
            vytexto = (FONTE.render("Vy: {:10.2f}".format(p.vy/f), True, PRETO))
        else:
            vytexto = FONTE.render(texto, True, CINZA)       
        Janela.blit(vxtexto, vxret)      
        Janela.blit(vytexto, vyret)

        #Pinta as estruturas
        for est in Estruturas:
            # pygame.draw.rect (superfície, cor, retângulo)
            pygame.draw.rect(Janela, PRETO, est)

        #Pinta o projétil
        #draw.circle( superfície, cor, centro (x,y), raio)
        pygame.draw.circle(Janela, VERDE, (int(p.pos[0]),int(p.pos[1])), p.raio)

        #Printa o alvo
        pygame.draw.rect(Janela, VERMELHO, alvo)

    else:                       # Se atingiu o alvo
        FIM = (FIMFONTE.render("ACERTOU!", True, PRETO))
        Janela.blit(FIM, (200,ALTURA/2,0,0))

    # Desenha a tela final
    pygame.display.update()                     # Atualiza porções da tela
    Relogio.tick(QPS)                           # Coloca um máximo de 40fps
