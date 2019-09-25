## Mecânica Clássica #2b
## Desenvolvido por:    Jhordan Silveira de Borba
## E-mail:              jhordandecacapava@gmail.com
## Website:             https://github.com/SapoGitHub
##                      https://alkasl.wordpress.com   
## 2019

import pygame                   # Biblioteca usada na criação de aplicações multimídia
from pygame.locals import *     # Várias constantes usadas pelo pygame
import sys                      # Biblioteca com funções relacionadas ao interpretador

# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------
pygame.init()                   # Inicializar todos o módulos importados do pygame
Relogio = pygame.time.Clock()   # Cria um objeto pra ajudar a rastrear o tempo
LARGURA = 600                   # Largura da tela
ALTURA = 600                    # Altura da tela
Janela = pygame.display.set_mode((LARGURA, ALTURA)) # Inicializa uma tela para exibit
pygame.display.set_caption('Corpos')                # Coloca um título para a tela

QPS=200                         # Quadros por segundo
Ligado =  False                 # Variáveis de controle

# Algumas cores
BRANCO = (255, 255, 255)
PRETO  = (0, 0, 0)

#Vamos ler o arquivo
n=0
pos_x=[]
pos_y=[]
tam=  100000000                 # Tamanho do arquivo
sim=  10000##500                # Quantidade dados reduzidos

arq=open("sim.txt","r")

k=0
for l in range(tam):
    linha = arq.readline()
    k=k+1
    if (n==sim):
        try:
            (x,y)=(linha.split(","))
        except:
            print('Quantidade de linhas: '+str(k))
            break
        pos_x.append(float(x))
        pos_y.append(float(y))        
        n=0
    n=n+1

pos=(300,300)

# 2 - ENTRADAS ------------------------------------------------------------------------------
while (True):
    # Vamos checar por eventos
    for evento in pygame.event.get():       # Pega eventos da fila
        if evento.type == QUIT:             # Se tentou fechar o jogo
            pygame.quit()                   # Fecha todos os módulos
            sys.exit()                      # Sai do Python
        if evento.type == KEYDOWN:          # Se apertou algum botão
            if (evento.key == K_RETURN):    # E foi enter
                if (Ligado == False):
                    Ligado=True
                    i=0
                else:
                    Ligado=False
                    i=0
                                    
# 3 - Motor de Física ---------------------------------------------------------------------------
    if (Ligado):                                    # Caso iniciamos a simulação
        pos=(int(pos_x[i]),int(pos_y[i]))
        i=i+1
        if (i>=len(pos_x)):
            Ligado=False

# 4 - Atualização da Tela ----------------------------------------------------------------------
    # Pinta o fundo
    Janela.fill(BRANCO)                         # Preenche a superfície com uma cor sólida

    # Pinta os corpos na tela
    pygame.draw.circle(Janela, PRETO, pos, 2)
    pygame.draw.circle(Janela, PRETO,(300,300), 10)

    # Desenha a tela final
    pygame.display.update()                     # Atualiza porções da tela
    Relogio.tick(QPS)                           # Coloca um máximo de 40fps
