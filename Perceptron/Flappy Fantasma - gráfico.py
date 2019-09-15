##PERCEPTRON: Flappy Fantasma - Gráfico de visualização
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Flappy-Fantasma
##2018


import matplotlib.pyplot as plt             #Biblioteca para plotar gráficos
import os                                   #Biblioteca relacionada a caminhos
from PIL import Image                       #PIL para trabalhar com as imagens
import matplotlib.animation as animation    #Para fazer animação

#Fundo de todos os gráficos
def fundo():
    #Salvamos os pontos no gráfico
    plt.scatter(voax, voay,s=4, c='red',label='Voa')
    plt.scatter(nvoax, nvoay,s=4,c='blue',label='Não Voa')
    plt.title("Aprendizado de um Perceptron")
    plt.xlabel('Altura do fantasma')
    plt.ylabel('Altura do obstáculo')
    ##Define limites nos eixos
    plt.ylim(ymin=0)                     
    plt.xlim(xmin=0)
    plt.xlim(xmax=5)
    plt.ylim(ymax=5)


#Cria o diretorio se não existe
if not os.path.exists("imagens/"):          #Se não existe
    os.makedirs("imagens/")                 #Cria

#Vamos ler os dados dos arquivos
with open("Peso1.txt", "r") as arquivo:     #Abrimos o arquivo
    p1 = []                                 #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        p1.append(line.rstrip('\n').replace(",", "."))        #Salvamos as linhas retirando as quebras e substituindo as vírgulas "," por pontos "."

with open("Peso2.txt", "r") as arquivo:     #Abrimos o arquivo
    p2 = []                                 #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        p2.append(line.rstrip('\n').replace(",", "."))        #Salvamos as linhas retirando as quebras e substituindo as vírgulas "," por pontos "."

with open("Limiar.txt", "r") as arquivo:    #Abrimos o arquivo
    L = []                                  #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        L.append(line.rstrip('\n').replace(",", "."))         #Salvamos as linhas retirando as quebras e substituindo as vírgulas "," por pontos "."

#Vamos criar os pontos no grafico:
voax=[]          #Array pra salvar os pontos na coordenada X que o passarinho voa
voay=[]          #Coordenada Y
nvoax=[]         #Array pra guardar os pontos que o passarinho não voa na coordenada X
nvoay=[]         #Coordenada Y

#Geramos os pontos
for x in range(0,50,1):             #Eixo X: Altura do fantasma
    for y in range (0,50,1):        #Eico Y: Altura do obstáculo
        if x>=y:                    #Se a altura do fantasma é maior ou igual que o obstáculo, não voa
            nvoax.append(x/10)
            nvoay.append(y/10)
        else:                       #Se não voa
            voax.append(x/10)
            voay.append(y/10)

n=0                                         #Variável pra indicar qual figura estamos salvando

fundo()                                     #Plotamos o fundo
plt.legend()                                #Inserimos as legendas
plt.savefig('imagens/fig-'+str(n)+'.png', bbox_inches='tight')   #Salvamos a figura com o fundo e removemos o possivel da borda
plt.show()                                  #Exibimos

#Vamos percorrer nossas matrizes agora
for x in range(11):
    xis=[]                                          #Onde vamos guardar as posições x
    yp=[]                                           #Onde vamos guardar as posições y
    y=-(float(p1[x])*0+float(L[x]))/float(p2[x])    #Equação da reta para encontrar a posição y para x=0, y(x=0)
    xis.append(0)                                   #Salvamos a posição x
    yp.append(y)                                    #Salvamos a posição y
    y=-(float(p1[x])*5+float(L[x]))/float(p2[x])    #Posição y para x = 5, y(x=5)
    xis.append(5)
    yp.append(y)
    fundo()                                         #Plotamos o fundo
    plt.plot(xis,yp,'black')                        #Plotamos uma linha entre os dois pontos
    plt.legend()
    plt.savefig('imagens/fig-'+str(n+1)+'.png', bbox_inches='tight')
    #plt.show()
    plt.close();                                    #Fechamos o plot atual
    n+=1                                            #Indicamos que salvamos mais uma figura

#Vamos criar um GIF
fig = plt.figure()                                  #Cria uma figura
ims = []                                            #Criamos nossa lista de frames
plt.axis('off')
for x in range(12):                                 #Vamos percorer as imagens que salvamos
    em = Image.open("imagens/fig-"+str(x)+".png")   #Carregamos as imagens
    im = plt.imshow(em, animated=True)              #Renderiza a imagem
    ims.append([im])                                  #Salvamos como um frame
ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True,repeat_delay=2000)    #Configuramos a animação
ani.save('imagens/animacao.gif')                    #Salvamos a animação
plt.show(ani)                                       #Plotamos a animação
