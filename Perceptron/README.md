# Perceptron

## Porta NAND

### Dados de treinamento

Uma porta lógica é uma porta que para uma par de entradas binárias (0 ou 1) retorna sempre 1 exceto se o par for (1,1), ou seja, possui a seguinte tabela verdade:
<pre>
Entrada A	Entrada B	Saída
0		0		1
0		1		1
1		0		1
1		1		0
</pre>
Esse é o conjunto de dados que vamos utilizar para treinar nossa rede, com a leve alteração que  como nossa saída é 1 ou -1, vamos trocar o 0 por -1 na saída, as entradas podem permanecer iguais.

### Função ativação

A função de ativação de um perceptron é dividida em duas partes, se a soma do produto do somatório entre as entradas e seus respectivos pesos, e seu limiar for maior que 0, retorna 1, caso contrário retorna -1. Isto é por exemplo,para duas entradas: se  <code>y=e<sub>1</sub>*p<sub>1</sub>+e<sub>2</sub>*p<sub>2</sub>+L</code> (<code>e<sub>1</sub></code> é a entrada 1, <code>p<sub>1</sub></code> é o peso 1 e <code>L</code> é o limiar do neurônio) o resultado for maio quer 0, então temos como saída 1, do contrário, a saída é -1.

### Aprendizagem

A aprendizagem é feita de acordo com a regra de aprendizagem do perceptron e deve ser feita a cada neurônio individualmente seguindo as regras:
- Se a saída está correta, não faz nada;
- Se a saída está errada, ajusta o peso com a seguinte fórmula: <code>p'<sub>i</sub>=p<sub>i</sub>+e<sub>i</sub>.d.n</code>.

Algumas observações importantes:
- <code>p'<sub>i</sub></code> é o novo peso enquanto <code>p<sub>i</sub></code> é o antigo;
- <code>d</code> é a saída desejada;
- O limiar é tratada como um peso de uma entrada que vale 1, então sua fórmula é simplesmente <code>L=L+d.n</code>;
- <code>n</code> é a taxa de aprendizagem, deve ser um valor real positivo de tal modo que não seja grande o suficiente pra impedir que o resultado seja atingido, nem pequeno o suficiente pra que se torne muito lento o processo.

Para poder medir o quão boa nossa rede esta, podemos definir uma função para isso, chamamos essa função de função custo.  Para nossa rede vamos utilizar o somatório das diferenças entre as saídas desejadas e as atuais para as 4 entradas de treinamento, ou seja, nossa função custo é <code>(d<sub>1</sub>-a<sub>1</sub>)²+(d<sub>2</sub>-a<sub>2</sub>)²+(d<sub>3</sub>-a<sub>3</sub>)²+(d<sub>4</sub>-a<sub>4</sub>)²</code>, onde <code>d<sub>i</sub></code> e <code>a<sub>i</sub></code> são nossas saídas desejadas e atuais respectivamente.

Com tudo definido, rodando meu código, obtive os seguintes valores:

Peso A: -0.02036<br>
Peso B: -0.01036<br>
Limiar: 0.030003

## Flappy Fantasma

Podemos visualizar graficamente a aprendizagem de uma rede, visualizando a reta formada a partir da equação que compõem a função de ativação igualda a zero, isto é, para nosso exemplo de duas entradas: <code>e<sub>1</sub>*p<sub>1</sub>+e<sub>2</sub>*p<sub>2</sub>+L=0</code>. Essa é uma equação da reta, e para uma rede bem treinada, deve separar perfeitamente os dois conjuntos de pontos, então podemos visualizar como a rede vai ajustando a reta conforme é treinada.

Com essa ideia em mente, vamos treinar uma rede para jogar Flappy Fantasma. Os dados de treinamento são todas as combinações possíveis para as posições do fantasma e do obstáculo entre 0 e 1, com uma variação de 0,1. Temos então 10 alturas possíveis para o fantasma, com 10 alturas possíveis pro obstáculo, ficamos com um total de 100 dados de treinamento.

E como condição de saída, vamos usar simplesmene que se a altura do fantasma é maior ou igual a do obstáculo, a saída é -1 (não voa), caso contrário, temos 1 (voa). Durante o processo de aprendizagem, vamos guardar os pesos e limiares.

E então escrevemos outro código para ler os valores e então manipulando nossa equação podemos obter os pontos Y a partir dos X. Considerando a entrada 1 como X, então a entrada 2 como Y, ficamos com <code>e<sub>2</sub>=-(e<sub>1</sub>*p<sub>1</sub>+L)/p<sub>2</sub></code>. A partir disso podemos pegar dois pontos e traçar uma reta entre eles.

A partir desse método, obtemos a seguinte imagem:

![Gráfico do Flappy Fantasma](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Perceptron/imagens/animacao.gif)

Podemos observar que o fato de termos treinado somente com valores entre 0 e 1, fez com que a rede mesmo apresentando uma taxa de acerto de 100% nessa faixa de valores, quando subimos para valores próximos a 5, começa a apresentar erros cada vez maiores. Se queremos utilizar nossa rede para valores nesta faixa maior, precisaríamos que os dados de treinamento fossem mais bem distribuídos durante toda a faixa.

## Porta OR

Apesar de não podermos treinar uma rede com perceptron com mais de uma camada, podemos combinar as redes treinadas individualmente para termos como resultado, uma rede mais complexa. Se com nossa rede anterior construímos uma porta NAND, podemos a partir de diferentes combinações obtermos toda a lógica NAND então.

Como por exemplo a porta OR, pode ser construída com 3 portas NAND com o seguinte esquema:
<pre>
Entrada A=O
	   \
	    O-Saída
	   /
Entrada B=O
</pre>
Onde cada <code>O</code> representa uma porta NAND. Ou seja, primeiro temos duas portas lógicas NAND que recebem uma entrada cada, mas duplamente. Então a saída de cada uma das portas NAND anteriores é a entrada para uma nova porta NAND, ou se.

Por exemplo,Então se nossa entrada da porta OR é 10, uma porta lógica NAND recebe 11 (retorna 0) e a outra porta recebe 00 (retorna 1). Então a última porta NAND recebe 01 e retorna 1.

Nossa rede pode seguir exatamente o mesmo esquema, substituindo onde temos uma porta lógica, por um neurônio treinado na etapa anterior.

A tabela verdade da porta OR é a seguinte:
<pre>
Entrada A	Entrada B	Saída
0		0		0
0		1		1
1		0		1
1		1		1
</pre>

## Projeto final

Podemos treinar uma rede neural também com duas saídas, se tivermos dois neurônios independentes e conhecermos a saída esperada de cada um deles separadamente para cada conjunto de entrada. Para respondar nossa questão proposta, "<b>produzo mais alimento?</b>" vamos imaginar um cenário simplificado de nosso antigo projeto:
	
### Primeira parte:

- O estoque de alimento varia de 0% a 100%;
- O número de famintos varia de 0 a 10.

Nessa primeira etapa, queremos que 1 signifique "atenção" e -1 signifique "tranquilo". Nossas regras são simples:
- Se estoque de alimento for menor 50%, significa atenção;
- Se o número de famintos for maior ou igual a 5, significa atenção.

Construimos uma rede com duas entradas e dois neurônios, chamaremos de rede 1.

### Segunda Parte

A partir dos resultados obtidos pela rede 1, estabelecemos o seguinte conjunto de regras para definir se vamos produzir ou não alimento:
<pre>
Comida		Colonos		Produz alimento?
Tranquilo	Tranquilo	Não
Tranquilo	Atenção		Sim
Atenção		Tranquilo	Sim
Atenção		Atenção		Sim
</pre>

Se prestar atenção, é idêntico a tabela verdade da porta OR, então tudo que precisamos é utilizar as saidas de nossa atual rede como entradas pra rede da porta lógica OR. Então ficamos com a seguinte rede neural:

![Imagem de uma rede neural](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Perceptron/imagens/final.png)

Onde as flechas mais grossas entre as redes indica uma entrada dupla.
