/*
PERCEPTRON: Projeto final
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
#include <locale.h>		//Biblioteca relacionada a localização



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

//Nossa redes OR
int rede_or(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada
	
	int temp[2];	//Variável pra guardar as saídas temporárias de nossa rede;
	int saida;		//Saída
	
	temp[0]=perceptron(peso,limiar,entradaA,entradaA);		//Entramos duas vezes a entrada A em nosso neurônio
	if (temp[0]==-1){temp[0]=0;}							//Nosso neurônio retorna -1, o que equivale a 0 em nossa entrada
	temp[1]=perceptron(peso,limiar,entradaB,entradaB);		//Entramos duas vezes a entrada B em nosso neurônio
	if (temp[1]==-1){temp[1]=0;}
	saida=perceptron(peso,limiar,temp[0],temp[1]);			//Entramos com os resultados anteriores nosso neurônio
	if (saida==-1){saida=0;}
	
	return saida;
}

float custo (int saida[2][250],int saida_atu[2][250]){
	//saida		- Matriz com as saidas corretas
	//saida_atu	- Matriz com as saidas atuais

	float costo;	//Onde vamos armazenar o resultado da função custo
	costo=0;
	int c,k;
	for (c=0;c<250;c++){
		costo=costo+pow(saida[0][c]-saida_atu[0][c], 2)+pow(saida[1][c]-saida_atu[1][c], 2);					//Calculamos todas saídas
	}	
	return costo;	//Retornamos o resultado
}

//Função para treinar a rede
float treinamento(float peso[][2], float *limiar){	
	//peso		- Matriz com os pesos das entradas dos neurônios
	//limiar 	- Limiar de saída dos neurônios
	
	int c,k,n;				//Variávelis auxiliares
	float taxa;				//Nossa taxa de aprendizado
	float cust;				//Vamos guardar o custo
	int s_esp[2][250];		//Saidas esperadas
	int s_atu[2][250];		//Saidas atuais
	float entA[250];		//EntradaA
	float entB[250];		//EntradaB
	
	//Vamos gerar os dados de treinamento
	n=0;									//Contador
	for (c=1;c<100;c+=2){					//Variar a porcentagem de comida de 1 até 100%, avançando de 2 em 2
		for (k=1;k<10;k+=2){				//Variar o número de famintos 1 até 10, avançando de 2 em 2
			entA[n]=c;						//Guardamos a porcentagem atual na entrada A
			entB[n]=k;						//E o número de famintos na entada B
			if (c>=50){s_esp[0][n]=-1;}		//Se a porcentagem for maior ou igual a 50, a saída esperada do primeiro neurônio é -1
			else {s_esp[0][n]=1;}			//Se não é 1
			if (k>=5){s_esp[1][n]=1;}		//Se a quantidade de famintos é maior ou igual a 5, a saída esperada do segundo neurônio é 1
			else {s_esp[1][n]=-1;}			//Se não é -1
			n++;							//Aumentamos o contador
		}	
	}

	//Colocamos valores iniciais para limiares e pesos
	for (c=0;c<2;c++){
		limiar[c]=1;
		for (k=0;k<2;k++){peso[c][k]=1;}
	}

	taxa=0.1;				//Definimos a taxa de aprendizado
	
    srand(time(NULL)); 		// Gera uma semente para os números aleatórios (srand) baseados no s segundos passados desde 01/01/1970 (time(NULL))
	
	//Vamos rodar uma vez todos os dados para obtermos a saída atual com estas entradas e pesos
	for (c=0;c<250;c++){													//Vamos adicionar uma contagem
		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de saída atual para o primeiro neurônio	
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de saída atual para o segundo neurônio
	}
	
	//E então vamos treinar de fato
	for (k=0;k<250000;k++){													//Vamos adicionar uma contagem
		c =rand() % 250;													//Sorteio um número entre 0 e 249

		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de saída do primeiro neurônio
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de saída do segundo neurônio
		
		if(s_atu[0][c]-s_esp[0][c]!=0){										//Checamos se a saída do primeiro neurônio está errada											
			peso[0][0]=peso[0][0]+taxa*s_esp[0][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[0][1]=peso[0][1]+taxa*s_esp[0][c]*entB[c];					//O segundo peso
			limiar[0]=limiar[0]+taxa*s_esp[0][c];							//E o limiar
		}
		
		if(s_atu[1][c]-s_esp[1][c]!=0){										//Checamos se a saída do segundo neurônio está errada	
			peso[1][0]=peso[1][0]+taxa*s_esp[1][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[1][1]=peso[1][1]+taxa*s_esp[1][c]*entB[c];					//O segundo peso
			limiar[1]=limiar[1]+taxa*s_esp[1][c];							//E o limiar
		}
		
		if (k==1000){														//A  cada 1000 cálculos
			cust = custo (s_esp,s_atu);										//Calculamos o custo
			if (abs(cust)<0.1){break;}										//Se temos um erro abaixo de um valor, saímos do loop
			k=0;															//Zeramos novamente k
		}				
	}
	return 0;													
}

//Vamos juntar nossas redes
int rede_final(float peso[][2], float *limiar,float *peso_or,float limiar_or,int entradaA,int entradaB){
	//peso			- Matriz com os pesos das entradas dos neurônios
	//limiar 		- Limiar de saída dos neurônios
	//peso_or		- Array com os pesos das entradas do neurônio da rede OR
	//limiar_or 	- Limiar de saída do neurônio da rede OR
	//entradaA		- Primeira entrada
	//entradaB		- Segunda entrada

	
	int temp[3];		//Variável para guardar os resultadods temporários
	temp[0]=perceptron(peso[0],limiar[0],entradaA,entradaB);			//Recebemos o primeiro valor de saída atual	da nossa rede 1
	temp[1]=perceptron(peso[1],limiar[1],entradaA,entradaB);			//Recebemos o primeiro valor de saída atual	da nossa rede 1
	//Convertemos as saídas -1 em 0
	if (temp[0]==-1){temp[0]=0;}
	if (temp[1]==-1){temp[1]=0;}
	temp[2]=rede_or(peso_or,limiar_or,temp[0],temp[1]); 				//Calculamos então a saída de nossa rede
	
	return temp[2]; 													//Retornamos
	
}

//Função principal
int main (){						
	 setlocale(LC_ALL, "Portuguese");		//Define o idioma como português para funcionar a acentuação
	 		
	//Pesos e limiares das portas lógicas
	float peso_or[2];						//Peso das duas entradas na porta NAND 
	float limiar_or;						//Limiar do neurônio na porta NAND
	//Pesos e limiares de nossa nova rede
	float peso[2][2];						//Pesos das duas entradas nos dois neurônios de nossa rede
	float limiar[2];						//Limiar dos dois neurônios
	
	int ent[2],res[2];						//entradas e saídas
	
	//Valores calculados em nosso outro código	
	peso_or[0]=-0.02036;
	peso_or[1]=-0.01036;
	limiar_or= 0.030003;
	
	//Vamos treinar nossa nova rede
	treinamento (peso,limiar);
	
	//Exibir os pesos e limiares calculados
	printf("NEURôNIO 1\n\n");
	printf("Peso A: %f\n",peso[0][0]);
	printf("Peso B: %f\n",peso[0][1]);
	printf("Limiar: %f\n",limiar[0]);
	printf("\n");
	printf("NEURÔNIO 2\n\n");
	printf("Peso A: %f\n",peso[1][0]);
	printf("Peso B: %f\n",peso[1][1]);
	printf("Limiar: %f\n",limiar[1]);
	printf("\n");
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Aguarda o pressionamento de uma tecla para continuar
	
	//Vamos interagir com o resultado de nossa nova rede
	ent[0]=1;
	ent[1]=0;
	while(ent[0]!=999 && ent[1]!=999){
		system("cls");												//Limpamos a tela
		printf( "PROJETO FINAL PT I\n");
		printf("Entre com 999 como entrada para avançar\n\n");
		printf( "Porcentagem de alimento:");
	    scanf("%d",&ent[0]);										//Recebemos a entrada A
	    printf( "Quantidade de famintos:");								
	    scanf("%d",&ent[1]);										//Recebemos a entrada B
		res[0]=perceptron(peso[0],limiar[0],ent[0],ent[1]);			//Recebemos o primeiro valor de saída atual	
		res[1]=perceptron(peso[1],limiar[1],ent[0],ent[1]);			//Recebemos o segundo valor de saída atual	
		if (res[0]==-1){ printf("Alimento: Tranquilo\n");}
		else { printf("Alimento: Atenção\n");}
		if (res[1]==-1){ printf("Colonos: Tranquilo\n\n");}
		else { printf("Colonos: Atenção\n\n");}
		printf("Pressione qualquer tecla para continuar");
		getchar();													//Consome a quebra de linha que sobrou do scanf
		getchar();													//Aguarda o pressionamento de uma tecla para continnuar
	}
	
	//Então conectamos nossas redes já treindas
	ent[0]=1;
	ent[1]=0;
	while(ent[0]!=999 && ent[1]!=999){
		system("cls");												//Limpamos a tela
		printf( "PROJETO FINAL PT II\n");
		printf("Entre com 999 como entrada para avançar\n\n");
		printf( "Porcentagem de alimento:");
	    scanf("%d",&ent[0]);										//Recebemos a entrada A
	    printf( "Quantidade de famintos:");								
	    scanf("%d",&ent[1]);										//Recebemos a entrada B
		res[0]=rede_final(peso,limiar,peso_or,limiar_or,ent[0],ent[1]);			//Recebemos o valor de saída atual	
		if (res[0]==1){printf("Saida: Produza alimento.\n\n");}
		else {printf("Saida: Não produza alimento.\n\n");}
		printf("Pressione qualquer tecla para continuar");
		getchar();													//Consome a quebra de linha que sobrou do scanf
		getchar();													//Aguarda o pressionamento de uma tecla para continnuar
	}

}
