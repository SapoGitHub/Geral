## Mecânica Clássica #2
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
import copy                     # Biblioteca para copiar os objetos

# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------
pygame.init()                   # Inicializar todos o módulos importados do pygame
Relogio = pygame.time.Clock()   # Cria um objeto pra ajudar a rastrear o tempo
LARGURA = 600                   # Largura da tela
ALTURA = 600                    # Altura da tela
Janela = pygame.display.set_mode((LARGURA, ALTURA)) # Inicializa uma tela para exibit
pygame.display.set_caption('Corpos')                # Coloca um título para a tela

QPS=200                         # Quadros por segundo
Ligado =  False                 # Variáveis de controle
dT=1/100                        # Intervalo dos passos
vmax= 100                       # Velocidade máxima inicial em cada eixo
G = 10000                    # Constante gravitacional

# Algumas cores
BRANCO = (255, 255, 255)
PRETO  = (0, 0, 0)


#Vamos definir nossos corpos
class Corpos:                 # A classe Corpos
    def __init__(self):
        self.vx   = random.randint(-vmax,vmax)                    # Sua velocidade no eixo x (em pixel/s)
        self.vy   = random.randint(-vmax,vmax)                    # Sua velocidade no eixo y (em pixel/s)
        self.pos  = (random.gauss(300, 50),random.gauss(300, 50)) # Sua localização
        self.raio = 2                                             # Raio
        self.ax   = 0                                             # Aceleração no eixo x
        self.ay   = 0                                             # Aceleração no eixo y
        self.m    = 1                                             # Massa
        

n=2                        # Quantidade de corpos
c=[]                        # Lista de corpos
for i in range(n):
    c.append(Corpos())      #Geramos nossos corpos

#Nosso corpo especial
c[0].m=100
c[0].raio=10
c[0].vx=0
c[0].vy=0
c[0].pos=(300,300)

#
c[1].pos=(300,200)
c[1].vx=100
c[1].vy=0
c[1].m=1/10000000000000000000000

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
    if (Ligado):                                    # Caso iniciamos a simulação
        velho=[]                                    # Vamos fazer um backup
        for elemento in c:                          # Copiamos elemento por elemento
            velho.append(copy.deepcopy(elemento))   # Precisamos achar função pra copiar objetos
        remov=[]                                    # Lista dos objetos que vamos renovar no final do quadro
        for i in range(n):                          # Vamos examinar cada corpo
            if (i not in remov):                    # Se não estiver na lista de remoção
                c[i].pos = ((c[i].pos[0]+c[i].vx*dT+c[i].ax*(dT*dT)/2),c[i].pos[1]+c[i].vy*dT+c[i].ay*(dT*dT)/2)    # Posição
                c[i].vx=c[i].vx+c[i].ax*dT                                                                          # Velocidade X
                c[i].vy=c[i].vy+c[i].ay*dT                                                                          # Velocidade Y

                #Vamos atualizar a aceleração
                ax=0                                            # Aceleração em X inicial
                ay=0                                            # Aceleração em Y inicial
                for m in range(n):                              # Vamos comparar com cada um dos corpos
                    if (i!= m):                                 # Desde que não seja o próprio corpo
                        dx= velho[m].pos[0]-velho[i].pos[0]     # Distância no eixo X
                        dy= velho[m].pos[1]-velho[i].pos[1]     # Distância no eixo Y
                        d=np.sqrt(dx*dx+dy*dy)                  # Distância total
                        if (d>(c[i].raio+c[m].raio)):           # Se não colidiram os corpos
                            ax=ax+dx*velho[m].m/(d*d*d)         # Atualizamos a aceleração em X
                            ay=ay+dy*velho[m].m/(d*d*d)         # Atualizamos a aceleração em Y
                        elif (m not in remov):                  # Se colidiu, com um corpo que já não vai se removido
                                #Vamos calcular as propriedades do nosso novo corpo
                                c[i].m = velho[m].m+velho[i].m                                                          # Massa
                                c[i].vx=(velho[i].m*velho[i].vx+velho[m].m*velho[m].vx)/(velho[i].m+velho[m].m)         # Velocidade X
                                c[i].vy=(velho[i].m*velho[i].vy+velho[m].m*velho[m].vy)/(velho[i].m+velho[m].m)         # Velocidade Y
                                c[i].raio=velho[i].raio+velho[m].raio                                                   # Raio
                                px=(velho[i].m * velho[i].pos[0] + velho[m].m * velho[m].pos[0])/(velho[i].m+velho[m].m)# Posição X
                                py=(velho[i].m * velho[i].pos[1] + velho[m].m * velho[m].pos[1])/(velho[i].m+velho[m].m)# Posição Y
                                c[i].pos=(px,py)                                                                        # Posição final
                                remov.append(m)                                                                         # Adicionamos o corpo na lista de remoção
                # A nova aceleração em cada eixo é o somatório anterior multiplicado pela constante gravitacional
                c[i].ax=G*ax                                
                c[i].ay=G*ay

#Vamos remover os itens que devem ser removidos:
        remov.sort()            # Ordenamos a lista
        m=0                     # Variável de controle
        for i in remov:         # Para cada item guardado
            c.remove(c[i-m])    # Removemos
            n=n-1               # Diminuimos a quantidade total
            m=m+1               # Os próximos elementos vão ser deslocados
            
        print(np.sqrt((c[0].pos[0]-c[1].pos[0])*(c[0].pos[0]-c[1].pos[0])+(c[0].pos[1]-c[1].pos[1])*(c[0].pos[1]-c[1].pos[1])))

# 4 - Atualização da Tela ----------------------------------------------------------------------
    # Pinta o fundo
    Janela.fill(BRANCO)                         # Preenche a superfície com uma cor sólida

    # Pinta os corpos na tela
    for corpo in c:
        pygame.draw.circle(Janela, PRETO, (int(corpo.pos[0]),int(corpo.pos[1])), corpo.raio)

    # Desenha a tela final
    pygame.display.update()                     # Atualiza porções da tela
    Relogio.tick(QPS)                           # Coloca um máximo de 40fps
