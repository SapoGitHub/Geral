/*
PERCEPTRON: Porta OR
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

//Nossa combinação de redes
int por(float *peso,float limiar,int entradaA,int entradaB){
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

int main (){								//Função principal
	float peso[2];							//Peso das duas entradas 
	float limiar;							//Limiar do neurônio
	int ent[2],res;							//entradas
	
	//Valores calculados em nosso outro código	
	peso[0]=-0.02036;
	peso[1]=-0.01036;
	limiar= 0.030003;
	
	//Interação	
	while(1){					//Para sair basta entrar com 99 em qualquer entrada
	system("cls");										//Limpamos a tela
	printf( "PORTA OR\n\n");
    printf( "Entrada A:");
    scanf("%d",&ent[0]);								//Recebemos a entrada A
    printf( "Entrada B:");								//Recebemos a entrada B
    scanf("%d",&ent[1]);
    res=por(peso,limiar,ent[0],ent[1]); 			//Calculamos então a saída de nossa rede
	printf("Saida: %d\n\n",res);
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Consome a quebra de linha que sobrou do scanf
	getchar();											//Aguarda o pressionamento de uma tecla para continnuar
	}	
}
