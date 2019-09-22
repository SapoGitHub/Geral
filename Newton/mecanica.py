## Mecânica Clássica
## Desenvolvido por:    Jhordan Silveira de Borba
## E-mail:              jhordandecacapava@gmail.com
## Website:             https://github.com/SapoGitHub
##                      https://alkasl.wordpress.com   
## 2019

import pygame                   # Biblioteca usada na criação de aplicações multimídia
import sys                      # Biblioteca com funções relacionadas ao interpretador
from pygame.locals import *     # Várias constantes usadas pelo pygame
import random                   # Biblioteca com números pseudo aleatórios
import numpy as np              # Biblioteca de funções matemáticas

# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------
pygame.init()                   # Inicializar todos o módulos importados do pygame
Relogio = pygame.time.Clock()   # Cria um objeto pra ajudar a rastrear o tempo
LARGURA = 600                   # Largura da tela
ALTURA = 600                    # Altura da tela
Janela = pygame.display.set_mode((LARGURA, ALTURA)) # Inicializa uma tela para exibit
pygame.display.set_caption('Corpos')                # Coloca um título para a tela

QPS=200                         # Quadros por segundo
Ligado =  False                 # Variáveis de controle
dT=1/200                         # Intervalo dos passos
vmax= 0                         # Velocidade máxima em módulo
M = 1                           # Massa habital
G = 100                           # Constante gravitacional

# Algumas cores
BRANCO = (255, 255, 255)
PRETO  = (0, 0, 0)


#Vamos definir nossos corps
class Corpos:                 # A classe Corpos
    def __init__(self,i):
        self.vx = random.randint(-vmax,vmax)                    # Sua velocidade no eixo x (em pixel/s)
        self.vy = random.randint(-vmax,vmax)                    # Sua velocidade no eixo y (em pixel/s)
        self.pos = (random.gauss(300, 50),random.gauss(300, 50))# Sua localização
        self.raio=2                                             # Raio
        self.ax = 0                                             # Aceleração no eixo x
        self.ay = 0                                             # Aceleração no eixo y
        self.m=M                                                # Massa
        

n=10            # Quantidade de corpos
c=[]            # Lista de corpos
for i in range(n):
    c.append(Corpos(i))

#Nosso corpo especial
#c[0].m=10000
#c[0].raio=10
c[0].vx=c[0].vy=0

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
        velho=c.copy()
        remov=[]
        for i in range(n):
            c[i].pos = ((c[i].pos[0]+c[i].vx*dT+c[i].ax*(dT*dT)/2),c[i].pos[1]+c[i].vy*dT+c[i].ay*(dT*dT)/2)   # Posição
            c[i].vx=c[i].vx+c[i].ax*dT                                                   # Velocidade X
            c[i].vy=c[i].vy+c[i].ay*dT                                                   # Velocidade Y
            ax=0
            ay=0
            for m in range(n):
                if (i!=m):
                    dx= velho[m].pos[0]-velho[i].pos[0]
                    dy= velho[m].pos[1]-velho[i].pos[1]
                    d=np.sqrt(dx*dx+dy*dy)
                    if (d>(c[i].raio+c[m].raio)):
                        ax=ax+dx*velho[m].m/(d*d*d)
                        ay=ay+dy*velho[m].m/(d*d*d)
                    else:
                        if (velho[i].raio>velho[m].raio):
                            c[i].m=velho[i].m+velho[m].m
                            c[i].vx=(velho[i].m*velho[i].vx+velho[m].m*velho[m].vx)/c[i].m
                            c[i].vy=(velho[i].m*velho[i].vy+velho[m].m*velho[m].vy)/c[i].m
                            c[i].raio=velho[i].raio+velho[m].raio
                            if (m not in remov):
                                remov.append(m)
                        else:
                            c[m].m=velho[i].m+velho[m].m
                            c[m].vx=(velho[i].m*velho[i].vx+velho[m].m*velho[m].vx)/c[m].m
                            c[m].vy=(velho[i].m*velho[i].vy+velho[m].m*velho[m].vy)/c[m].m
                            c[m].raio=velho[i].raio+velho[m].raio
                            if (i not in remov):
                                remov.append(i)
#                        ax=0
#                        ay=0
#                        c[i].vx=0
#                        c[i].vy=0
                        break
            c[i].ax=G*ax
            c[i].ay=G*ay

#Vamos remover os itens que devem ser removidos:
        for i in remov:
            c.remove(c[i])
            n=n-1
            
# 4 - Atualização da Tela ----------------------------------------------------------------------
    # Pinta o fundo
    Janela.fill(BRANCO)             # Preenche a superfície com uma cor sólida

    #Pinta os corpos
    for corpo in c:
        pygame.draw.circle(Janela, PRETO, (int(corpo.pos[0]),int(corpo.pos[1])), corpo.raio)
#    pygame.draw.circle(Janela, VERMELHO, (830,580), 10)                         #Alvo opcional

    # Desenha a tela final
    pygame.display.update()                     # Atualiza porções da tela
    Relogio.tick(QPS)                           # Coloca um máximo de 40fps
