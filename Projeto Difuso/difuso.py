##PROJETO DIFUSO
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-Difuso
##2018

#Importar bibliotecas
import numpy as np                  #Numpy para operações matemáticas
import matplotlib.pyplot as plt     #Matplotlib para plotar os gráficos

#Função para desenhar as retas crescentes ou decrescentes
def reta (ini,fim,reso,tipo):
    #ini - Valor X inicial da reta // 0: Valor inicial Y da reta se crescente
    #fim - Valor X final da reta   //  1 Valor final Y da reta se crescente

    #Variáveis auxiliares
    final=[]
    x=[]
    y=[];

    if(tipo=="/"):
        yini=0
        yfim=1
    elif (tipo=="\\"):
        yini=1
        yfim=0
    elif (tipo=="-"):
        yini=0
        yfim=0
 
    inc=(yfim-yini)/(fim-ini) #Inclinação da reta

    #Equação da reta: inc=(y1-y0)/(x1-x0) -> y1=inc(x1-x0)+y0
    for n in range (ini,fim+1,+1):         #Vamos variar o x
        if (n!=fim):
            for m in range (0,reso):    #Dependendo da resolução vamos gradualmente
                xatu=n+m/reso
                yatu=inc*(xatu-ini)+yini
                x.append(xatu)
                y.append(yatu)
        else:
            x.append(fim)
            y.append(yfim)
            
    final.append(x)
    final.append(y)
    return final

##VAMOS CRIAR OS GRÁFICOS--------------------------------------------------------------------------------------------

#Vamos plotar o gráfico do estoque
#Baixo
x1=reta(0,50,100,'\\')
x2=reta(50,100,100,'-')
estoque_baixo=[[],[]]
estoque_baixo[0]=x1[0]+x2[0]
estoque_baixo[1]=x1[1]+x2[1]
plt.plot(estoque_baixo[0], estoque_baixo[1], 'red',label='Vazio')

#Medio
x1=reta(0,50,100,'/')
x2=reta(50,100,100,'\\')
estoque_medio=[[],[]]
estoque_medio[0]=x1[0]+x2[0]
estoque_medio[1]=x1[1]+x2[1]
plt.plot(estoque_medio[0], estoque_medio[1], 'blue',label='Médio')

#Cheio
x1=reta(0,50,100,'-')
x2=reta(50,100,100,'/')
estoque_cheio=[[],[]]
estoque_cheio[0]=x1[0]+x2[0]
estoque_cheio[1]=x1[1]+x2[1]
plt.plot(estoque_cheio[0], estoque_cheio[1], 'green',label='Cheio')

plt.xlabel('% do estoque cheio')
plt.title("Estoque de Alimento")
plt.legend()
plt.show()

#Vamos plotar o gráfico de famintos
#Poucos
x1=reta(0,5,100,'\\')
x2=reta(5,10,100,'-')
famintos_poucos=[[],[]]
famintos_poucos[0]=x1[0]+x2[0]
famintos_poucos[1]=x1[1]+x2[1]
plt.plot(famintos_poucos[0], famintos_poucos[1], 'green',label='Poucos')

#Medio
x1=reta(0,5,100,'/')
x2=reta(5,10,100,'\\')
famintos_medio=[[],[]]
famintos_medio[0]=x1[0]+x2[0]
famintos_medio[1]=x1[1]+x2[1]
plt.plot(famintos_medio[0], famintos_medio[1], 'blue',label='Médio')

#Cheio
x1=reta(0,5,100,'-')
x2=reta(5,10,100,'/')
famintos_muitos=[[],[]]
famintos_muitos[0]=x1[0]+x2[0]
famintos_muitos[1]=x1[1]+x2[1]
plt.plot(famintos_muitos[0], famintos_muitos[1], 'red',label='Muitos')

plt.xlabel('Quantidade de colonos famintos')
plt.title("Colonos Famintos")
plt.legend()
plt.show()
    
#Vamos plotar o gráfico de prioridade
#Poucos
x1=reta(1,5,100,'\\')
x2=reta(5,9,100,'-')
nivel_baixo=[[],[]]
nivel_baixo[0]=x1[0]+x2[0]
nivel_baixo[1]=x1[1]+x2[1]
plt.plot(nivel_baixo[0], nivel_baixo[1], 'green',label='Baixo')

#Medio
x1=reta(1,5,100,'/')
x2=reta(5,9,100,'\\')
nivel_medio=[[],[]]
nivel_medio[0]=x1[0]+x2[0]
nivel_medio[1]=x1[1]+x2[1]
plt.plot(nivel_medio[0], nivel_medio[1], 'blue',label='Médio')

#Cheio
x1=reta(1,5,100,'-')
x2=reta(5,9,100,'/')
nivel_alto=[[],[]]
nivel_alto[0]=x1[0]+x2[0]
nivel_alto[1]=x1[1]+x2[1]
plt.plot(nivel_alto[0], nivel_alto[1], 'red',label='Alto')

plt.title("Nível de prioridade")
plt.legend()
plt.show()

##VAMOS PEGAR OS NÍVEIS---------------------------------------------------------------------------------------

#Vamos informar a situação do estoque e a quantidade de famintos
estoque=75
famintos=7

print('Nível do estoque: '+str(estoque)+'%')
print('Quantidade de famintos: '+str(famintos))

#Vamos Pegar um valor para cada variável:
#Etoque
#Estoque vazio
c=0
for x in estoque_baixo[0]:
    if x==estoque:
        est_bai=estoque_baixo[1][c]
    c+=1

#Estoque medio
c=0
for x in estoque_medio[0]:
    if x==estoque:
        est_med=estoque_medio[1][c]
    c+=1

#Estoque cheio
c=0
for x in estoque_cheio[0]:
    if x==estoque:
        est_chei=estoque_cheio[1][c]
    c+=1

#Famintos
#Famintos poucos
c=0
for x in famintos_poucos[0]:
    if x==famintos:
        fam_pou=famintos_poucos[1][c]
    c+=1
    
#Famintos médio
c=0
for x in famintos_medio[0]:
    if x==famintos:
        fam_med=famintos_medio[1][c]
    c+=1

#Famintos muitos
c=0
for x in famintos_muitos[0]:
    if x==famintos:
        fam_mui=famintos_muitos[1][c]
    c+=1

print('')
print('Estoque vazio: '+str(est_bai))
print('Estoque médio: '+str(est_med))
print('Estoque cheio: '+str(est_chei))
print('')
print('Famintos poucos: '+str(fam_pou))
print('Famintos medios: '+str(fam_med))
print('Famintos muitos: '+str(fam_mui))

##VAMOS ATIVAR AS REGRAS--------------------------------------------------------------------------------------------
#Primeiro vamos pegar os valores das regras

#Primeira regra:
#Quando temos OU pegamos o máximo valor:
if est_bai>fam_mui:
    primeira=est_bai
else:
    primeira=fam_mui

#Segunda regra
segunda= est_med

#Terceira regra:
if est_chei>fam_pou:
    terceira=est_chei
else:
    terceira=fam_pou

print('')
print('Primeira regra: '+str(primeira))
print('Segunda regra: '+str(segunda))
print('Terceira regra: '+str(terceira))

#Então aplicamos as regras
#Conectamos a primeira regra a prioridade alta eliminando todos Y maiores que o valor:

for c in range(len(nivel_alto[1])):
    if (nivel_alto[1][c]>primeira):
        nivel_alto[1][c]=primeira

#Conectamos a segunda regra ao nivel medio
for c in range(len(nivel_alto[1])):
    if (nivel_medio[1][c]>segunda):
        nivel_medio[1][c]=segunda

#Conectamos a terceira regra ao nivel baixo
for c in range(len(nivel_alto[1])):
    if (nivel_baixo[1][c]>terceira):
        nivel_baixo[1][c]=terceira

#Plotando o gráfico
plt.plot(nivel_baixo[0], nivel_baixo[1], 'green',label='Baixo')
plt.plot(nivel_medio[0], nivel_medio[1], 'blue',label='Médio')
plt.plot(nivel_alto[0], nivel_alto[1], 'red',label='Alto')
plt.title("Nível de prioridade cortado")
plt.xlim(xmax=9)
plt.ylim(ymax=1)
plt.legend()
plt.show()

#COMBINAÇÃO----------------------------------------------------------------------
#Vamos combinar agora os resultados:
comb=[[],[]]
for c in range(len(nivel_alto[1])):
    x=nivel_alto[0][c]
    y=nivel_alto[1][c]+nivel_medio[1][c]+nivel_baixo[1][c]
    comb[0].append(x)
    comb[1].append(y)

plt.plot(comb[0], comb[1])
plt.title("Nível de prioridade combinado")
plt.ylim(ymin=0)
plt.show()

#Desfuzzificação---------------------------------------------------------------
#Então vamos obter uma resposta pro mendo real utilizando o método do centroide
#Como nosso gráfico é composto na verdade de vários pontos, vamos considerar
#pontos de massa sobre o eixo X igualmente espaçados, onde o Y corresponde aos
#Seus pesos e então vamos calcular o centro de massa
#cm=(m1x1+m2x2)/M

cm=0
M=0
c=0

for x in (comb[0]):
    cm=cm+x*comb[1][c]
    M=M+comb[1][c]
    c+=1

cm=cm/M

#Printando
plt.plot(comb[0], comb[1])
plt.plot([cm,cm],[0,1])
plt.title("Centro de massa do nível de prioridade")
plt.ylim(ymin=0)
plt.show()

#E arredondando:
cmar=round(cm,0)
print('')
print("Nível de prioridade definido: "+str(cmar))
