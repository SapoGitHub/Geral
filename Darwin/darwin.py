##DARWIN
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Darwin
##2018

import random   #Biblioteca para utilizar os comandos aleatorios

#Função para criar os lutadores iniciais
def inicia(n):
#n      - Número de lutadores
    
    lt=[]                           #Matriz para criar os lutadores

    for x in range(n):              #Loop para criar todos os lutadores
        #Atributos do lutador em questão
        att=[0,0,0,0]               #[Força, Constituição, Agilidade, Destreza]
        for y in range (100):       #Vamos distribuir 100 pontos
            z=random.randint(0,3)   #Sorteamos aonde vamos adicionar
            att[z]=att[z]+1         #Adicionamos

        lt.append(att)              #E salvar os atributos

    return lt                               #Retornamos os lutadores

#Função para fazer a luta entre 2 lutadores
def luta(lt):
#lt     - Matriz com os dois lutadores
#        [0][0]  Dano do lutador 1
#        [0][1]  Vida do lutador 1
#        [0][2]  Taxa de evasão do lutador 1
#        [0][3]  Taxa de acerto critico do lutador 1

##        #E atribuimos as estatísticas de acordo com nossa configuração
##        dano=1+att[0]
##        vida=10+10*att[1]
##        evasao=0+0.1*att[2]
##        critico=0+0.1*att[3]

    #Vamos ver quantos atributos cada lutador tem
    at1=lt[0][0]+lt[0][1]+lt[0][2]+lt[0][3]
    at2=lt[1][0]+lt[1][1]+lt[1][2]+lt[1][3]

    if (at1>100 and at2<=100):      #Se o primeiro passa de 100
        return 1                    #O segundo venceu
    elif (at1<=100 and at2>100):    #Se o segundo passa de 100
        return 0                    #O primeiro venceu
    elif (at1>100 and at2>100):     #Se os dois passam de 100
        if (at1<at2):               #Vence o que passou por menos
            return 0
        else:
            return 1
        

    #Dano dos lutadores
    atk1=1+lt[0][0]
    atk2=1+lt[1][0]

    #Vida inicial de nossos lutadores
    vid1=10+10*lt[0][1]
    vid2=10+10*lt[1][1]

    #Evasão de nossos lutadores
    eva1=0+0.1*lt[0][2]
    eva2=0+0.1*lt[1][2]

    #Critico de nossos lutadores
    c1=0+0.1*lt[0][3]
    c2=0+0.1*lt[1][3]

    
    #Vamos fazer os dois se enfrentarem de fato
    while(True):

        
        #Calculamos se os lutadores tiveram sucesso na evasão
        ev1=random.randint(1,101)       #Sorteamos um número de 1 a 100
        ev2=random.randint(1,101)     
        Ev1=Ev2=False
        if (ev1<=eva1):           #Se a taxa de evasão dos lutadores é por exemplo 5%, precisamos ter tirado abaixo ou igual a 5
            Ev1=True
        if (ev2<=eva2):
            Ev2=True
            
        #Se o lutador 2  não teve sucesso na evasão, calculamos o dano do lutador 1
        if (Ev2==False):
            Cr1=False
            cr1=random.randint(0,100)   #De modo análogo à evasão
            if (cr1<=c1):       #Fazemos o mesmo com a taxa de acerto crítico
                Cr1=True

            if (Cr1==True):             #Então, se teve crítico dobramos o ataque
                atk1=1+2*lt[1][0]
        else:                           #Se teve evasão, o dano é 0
            atk1=0

        #O mesmo para o lutador 2
        #Se o lutador 1  não teve sucesso na evasão, calculamos o dano do lutador 2
        if (Ev1==False):
            Cr2=False
            cr2=random.randint(0,100)   #De modo análogo à evasão
            if (cr2<=c2):       #Fazemos o mesmo com a taxa de acerto crítico
                Cr2=True

            if (Cr2==True):             #Então, se teve crítico dobramos o ataque
                atk2=1+2*lt[1][0]
        else:                           #Se teve evasão, o dano é 0
            atk2=0

        #Então computamos os danos dos ataques na vida
        vid1=vid1-atk2
        vid2=vid2-atk1
        
        #A luta termina quando algum dos dois lutadores ficar com vida abaixo de 0
        if (vid1<=0 or vid2<=0):
            if (vid1>vid2):             #O que ficou com mais vida vence
                return 0
            else:
                return 1
            
#Função para fazer todos lutadores lutarem entre si
def armaggedon(lutadores):
#lutadores      - Matriz com todos os lutadores

    res=len(lutadores)*[0]      #Lista com a quantidade de vitorias de cada lutador
    id1=0                       #ID do primeiro lutador
    for x in (lutadores):            #Fazemos o lutador X
        id2=0                        #ID do segundo lutador
        for y in (lutadores):        #Lutar com todos os lutadores y
            if (x!=y):                          #Se não for o mesmo lutador
                lucha=[]                        #Matriz com apenas os dois lutadores em questão
                lucha.append(x)                 #Adicionamos o primeiro lutador
                lucha.append(y)                 #Adicionamos o segundo lutador
                venc=luta(lucha)                #Descobrimos quem venceu
                if (venc==0):                   #Se retornou 0
                    res[id1]+=1                 #O lutador X venceu
                else:
                    res[id2]+=1                 #Se não foi o lutador Y
            id2+=1
        id1+=1
    return res

#Função para selecionar os campeões
def selecao(resultados):
#resultados     - Array com a quantidade de vitórias que cada indivíduo teve
    
    vencedores=[]                               #Onde vamos salvar os vencedores
    for x in range(int(len(resultados)/2)):          #Vamos salvar metade
        maior=None                              #Onde vamos salvar o maior valor
        for n in range(len(resultados)):
            if (maior==None):                   #Se é o primeiro valor
                maior=n                         #Salvamos
            elif (resultados[maior]<resultados[n]):         #Se não, mas é maior que o nosso salvo
                maior=n                         #Salvamos
                
        resultados[maior]=-1                    #Antes de irmos para o proximo campeão, eliminamos as vitórias do campeão salvo
        vencedores.append(maior)                #E salvamos o maior

    return vencedores                       #Retornamos os vencedores
                
#Funçao para cruzar os indivíduos
def cruzamento(campeoes,luchadores):
#campeoes       - Array com os lutadores selecionados pro cruzamento
#luchadores     - Matriz com os dados dos lutadores

    novos=[]    #Matriz com a nova população
    
    #Primeiro vamos salvar os indivíduos selecionados
    for x in range ((int(len(luchadores)/2))):
        lutador=luchadores[campeoes[x]]
        novos.append(lutador)
        
    #E gerar novos indivíduos
    for x in range ((int(len(luchadores)/2))):

        #Vamos sortear os 2 pais
        pai1=random.randint(0,len(campeoes)-1)      #Sorteamos o primeiro pai
        pai2=pai1
        while (pai1==pai2):                         #Queremos que os pais sejam individuos diferentes
            pai2=random.randint(0,len(campeoes)-1)  #Sorteamos o pai 2
            
        #Vamos sortear as duas caracteristica que vai herdar do primeiro pai
        car1=random.randint(0,3)
        car2=car1
        while (car1==car2):                         #Garantir que seja duas caracteristicas diferentes
            car2=random.randint(0,3)

        #E vamos finalmente distribuir as caracteristicas pro novo jogador
        lutador=[]
        for y in range(4):
            if (y==car1 or y==car2):            #Se e uma das caracteristicas sorteadas pro pai 1
                lutador.append(luchadores[campeoes[pai1]][y])   #Copiamos do pai 1
            else:                               #Se não
                lutador.append(luchadores[campeoes[pai2]][y])   #Copiamos do pai 2
        
        #Vamos testar a probabilidade de ocorrer uma mutação
        mut=random.randint(1,100)
        if(mut<10):             #Vamos considerar uma probabilidade de mutação de 100%
            x=random.randint(0,3);                          #Sorteamos um valor para diminuir o atributo
            k=random.randint(1,10)                          #Variando de 1 a 10
            if (lutador[x]-k>=0):                              #Se ainda podemos diminuir este atributo
                if (x%2==0):
                    c=k#random.randint(1,5)                  #Se for par, somamos 
                else:
                    c=-k#random.randint(1,5)                 #Se for ímpar, diminuimos 1
                    
                lutador[x]=lutador[x]+c                     #E de fato diminuimos outro atributo aleatório
                
        novos.append(lutador)                                   #Adicionamos o lutador na matriz dos novos
    return novos                                                #Retornamos a nova população    

#Função para testar o campeão
def teste(melhor):
    #Vamos testar contra um inimigo aleatorio qualquer:
    inimigo=inicia(1)
    #Vamos juntar os dois
    confronto=[]
    confronto.append(melhor)
    confronto.append(inimigo[0])
    #E fazemos o confronto
    x=luta(confronto)
    if (x==0):
        return 1        #Retornamos 1 se nosso campeão venceu
    else:
        return 0        #Retornamos 0 se perdeu

    
#Começa o codigo
populacao=inicia(8)                             #Criamos nossa população inicial

n=10000     #Número de gerações

for x in range(n):
##    if (x%1000==0):
##        print(x)
        
    resultados=armaggedon(populacao)                #Fazemos todos lutar contra todos
    campeoes=selecao(resultados)                    #Fazer a seleção dos melhores
    populacao2=cruzamento(campeoes,populacao)        #Cruzar os melhores para gerar novos descendentes
    populacao=populacao2

#Vamos checar o campeão
final=armaggedon(populacao)
campeao=selecao(resultados)
melhor=populacao[campeao[0]]
print("\nATRIBUTOS\n")     
print("Força: "+ str(melhor[0]))
print("Constituição: "+ str(melhor[1]))
print("Agilidade: ", (melhor[2]))
print("Destreza: ",(melhor[3]))

#Vamos ver uma porcentagem de vitorias
c=0
for k in range (1000):
    c=c+teste (melhor)

print("\n"+str((c/1000)*100)+"% de chance de vitória contra inimigo aleatório")
