## Raio do Círculo por Monte Carlo
## Desenvolvido por:    Jhordan Silveira de Borba
## E-mail:              jhordandecacapava@gmail.com
## Website:             https://github.com/SapoGitHub
##                      https://alkasl.wordpress.com   
## 2019

import pygame, sys, random      #Biblioteca usada na criação de aplicações multimídia
from pygame.locals import *     #Várias constantes usadas pelo pygame

# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------
pygame.init()                   # Inicializar todos o módulos importados do pygame
Relogio = pygame.time.Clock()   # Cria um objeto pra ajudar a rastrear o tempo
LARGURA = 600                   # Largura da tela
ALTURA = 600                    # Altura da tela
Janela = pygame.display.set_mode((LARGURA, ALTURA)) # Inicializa uma tela para exibit
pygame.display.set_caption('Fase 1')                # Coloca um título para a tela

QPS=120                         # Quadros por segundo
Ligado =  False                 # Variáveis de controle
f=100
g=9.81                        # Gravidade (convertida para pixel / s²)
dT=1/100                        # Intervalo dos passos (m*s/pixel*quadro)

# Algumas cores
BRANCO = (255, 255, 255)
VERDE  = (0, 255, 0)

#Vamos definir nosso projétil
class Projetil:                 # A classe projetil
    def __init__(self):
        self.vx = 45             # Sua velocidade no eixo x (em pixel/s)
        self.vy = 45            # Sua velocidade no eixo y (em pixel/s)
        self.pos = (15,580)     # Sua localização
        self.raio=5
        
p = Projetil()                  # Declaramos o objeto

# 2 - ENTRADAS ------------------------------------------------------------------------------
while True:
    # Vamos checar por eventos
    for evento in pygame.event.get():       # Pega eventos da fila
        if evento.type == QUIT:             # Se tentou fechar o jogo
            pygame.quit()                   # Fecha todos os módulos
            sys.exit()                      # Sai do Python
        if evento.type == KEYDOWN:          # Se apertou algum botão
            if (evento.key == K_RETURN):    # E foi enter
                Ligado=True
                                    
# 3 - Motor de Física ---------------------------------------------------------------------------
    if (Ligado):
        p.pos = ((p.pos[0]+p.vx*dT),p.pos[1]-p.vy*dT-g*(dT*dT)/2) # MRU
        p.vy=p.vy-g*dT                                            # MRUV

# 4 - Atualização da Tela ----------------------------------------------------------------------
    # Pinta o fundo
    Janela.fill(BRANCO)             # Preenche a superfície com uma cor sólida

    #Pinta o projé til
    pygame.draw.circle(Janela, VERDE, (int(p.pos[0]),int(p.pos[1])), p.raio)

    # Desenha a tela final
    pygame.display.update()                     # Atualiza porções da tela
    Relogio.tick(QPS)                           # Coloca um máximo de 40fps

