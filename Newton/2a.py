## Mecânica Clássica #2a
## Desenvolvido por:    Jhordan Silveira de Borba
## E-mail:              jhordandecacapava@gmail.com
## Website:             https://github.com/SapoGitHub
##                      https://alkasl.wordpress.com   
## 2019

import random                   # Biblioteca com números pseudo aleatórios
import numpy as np              # Biblioteca de funções matemáticas
import copy                     # Biblioteca para copiar os objetos

# 1 - CONFIGURAÇÃO --------------------------------------------------------------------------------
dT=1/1000000
G = 10000                    # Constante gravitacional
vmax= 100                       # Velocidade máxima inicial em cada eixo

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


#Vamos abrir o arquivo
arq=open("sim.txt","w")

# 2 - ENTRADAS ------------------------------------------------------------------------------
l=p=0
for k in range(100000000):
                                    
# 3 - Motor de Física ---------------------------------------------------------------------------
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

    arq.write(str(c[1].pos[0])+","+str(c[1].pos[1])+"\n")
    if (l==10000):
        p=p+0.01
        print(str(p)+'%')
        l=0
    l=l+1
            
arq.close()
