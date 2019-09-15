/*
PERCEPTRON: Porta NAND
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Perceptron
##2018
*/

#include <stdio.h>		//Biblioteca padrão de entradas e saídas
#include <stdlib.h>     //Biblioteca genérica, utilizada para srand, rand
#include <time.h>       //Biblioteca relacionada a data, utilizada para time
#include <math.h>		//Biblioteca com funções matemáticas

//Nosso neurônio
int perceptron(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	float res;	//Resultado parcial
	
	//Função de ativação
	res=entradaA*peso[0]+entradaB*peso[1]+limiar;
	
	if (res>0){
		return 1;
	}
	else{
		return -1;
	}
}

//Função custo
float custo_nand (int *saida, float *peso,float limiar,int *entradaA,int *entradaB){
	//saida		- Array com as saidas corretas
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	int res[4];		//Variável pra armazenar as respostas calculadas
	int c;			//Variável de controle
	float custo;	//Onde vamos armazenar o resultado da função custo
	
	for (c=0;c<4;c++){
		res[c]=perceptron(peso,limiar,entradaA[c],entradaB[c]);					//Calculamos todas saídas
	}
	
	custo= pow(res[0]-saida[0], 2)+pow(res[1]-saida[1],2)+pow(res[2]-saida[2],2)+pow(res[3]-saida[3],2);	//Função custo
	
	return custo;	//Retornamos o resultado
}

float treinamento_nand(float *peso, float limiar){	//Função para treinar a rede
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio

	int c,k;				//Variávelis auxiliares
	int res;				//Resultado de saida
	float taxa;				//Nossa taxa de aprendizado
	float cust;				//Vamos guardar o custo
	
	//Vamos gerar os dados de treinamento
	int entradaA[4];		//Entrada A
	int entradaB[4];		//Entrada B
	int saida[4];			//Saida
	
	//TABELA VERDADE
	entradaA[0]=0;	entradaB[0]=0;	saida[0]=1;
	entradaA[1]=0;	entradaB[1]=1;	saida[1]=1;
	entradaA[2]=1;	entradaB[2]=0;	saida[2]=1;
	entradaA[3]=1;	entradaB[3]=1;	saida[3]=-1; 						//Nossa saída é apenas 1 e -1, então vamos converter 0 para -1
	
	//Colocamos valores iniciais
	peso[0]=20;
	peso[1]=20;
	limiar=3;
	taxa=0.01;
	
    srand(time(NULL)); //  Gera uma semente para os números aleatórios (srand) baseados no s segundos passados desde 01/01/1970 (time(NULL))
	
	//E então 
	for (c=0;c<11;c++){													//Vamos adicionar uma contagem
	
		k =rand() % 4;													//Sorteio um número entre 0 e 3
		res=perceptron(peso,limiar,entradaA[k],entradaB[k]);			//Recebemos o valor de saída atual	
		if(res-saida[k]!=0){											//Checamos se a saída está errada											
			peso[0]=peso[0]+taxa*saida[k]*entradaA[k];					//Se estiver atualizamos o primeiro peso
			peso[1]=peso[1]+taxa*saida[k]*entradaB[k];					//O segundo peso
			limiar=limiar+taxa*saida[k];								//E o limiar
		}
		
		if (c==10){														//A  cada 10 cálculos
			cust = custo_nand (saida,peso,limiar,entradaA,entradaB);	//Calculamos o custo
			if (cust<0.1){break;}										//Se temos um erro abaixo de um valor, saímos do loop
			//Apenas um erro significa (1-(-1))²=2²=4, então qualquer valor abaixo de 4 satisfaz o que queremos
			c=0;														//Zeramos novamente c
		}				
	}
	return limiar;														//Retornamos apenas o limiar, o peso é um ponteiro, já foi alterado
}


int main (){								//Função principal
	float peso[2];							//Peso das duas entradas 
	float limiar;							//Limiar do neurônio
	int ent[2],res;							//entradas
		
	limiar = treinamento_nand(peso,limiar);		//Vamos primeiro treinar a rede do NAND
	
	//Exibir os pesos e limiares calculados
	printf("PERCEPTRON\n\n");
	printf("Peso A: %f\n",peso[0]);
	printf("Peso B: %f\n",peso[1]);
	printf("Limiar: %f\n",limiar);
	printf("\n\n");
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Aguarda o pressionamento de uma tecla para continuar
	
	//Interação	
	while(1){					//Para sair basta entrar com 99 em qualquer entrada
	system("cls");										//Limpamos a tela
	printf( "PORTA NAND\n\n");
    printf( "Entrada A:");
    scanf("%d",&ent[0]);								//Recebemos a entrada A
    printf( "Entrada B:");								//Recebemos a entrada B
    scanf("%d",&ent[1]);
    res=perceptron(peso,limiar,ent[0],ent[1]); 			//Calculamos então a saída de nossa rede
    if (res==-1){res=0;}					  			//Se for o caso, convertemos a nossa saída de -1 para 0
	printf("Saida: %d\n\n",res);
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Consome a quebra de linha que sobrou do scanf
	getchar();											//Aguarda o pressionamento de uma tecla para continnuar
	}	
}
