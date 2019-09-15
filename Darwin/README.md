# Darwin


## Mundo

Para começar nosso projeto, vamos configurar nosso mundo. Os lutadores inicialmente possuem o seguinte perfil:
<pre>
Dano: 	 1	Força:		0
Vida: 	 10	Constituiçao:	0
Evasão:  0%	Agilidade:	0
Crítico: 0%	Destreza:	0
</pre>
Então para cada nível novo nos atributos, nossas habilidades variam conforme os valores a seguir:

- Força:		+ 1 Dano
- Constituição:	+ 10 Vida
- Agilidade	+ 0.1% Evasão
- Destreza:	+ 0.1% Crítico

Os ataques de ambos os lutadores acontecem simultâneamente, e a luta se encerra quando um dos lutadores fica com vida abaixo de 0. Em caso de ambos os lutadores ficarem com vida negativa, vence aquele com a vida mais próxima de 0.

### População inicial

Nossa 1ª geração vai ser composta por 8 indivíduos com 100 pontos distribuídos de forma aleatória.


## Aptidão

Com uma população em mãos, devemos então descobrir o quão aptos eles são, isto é, o quão se aproximam do nosso objetivo. Como noss objetivo é distribuir os pontos da melhor forma possível, significa vencer a maior porcentagem das lutas possíveis. Como vamos colocar todos indivíduos para lutar contra todos, todos terão o mesmo número de lutas, e vamos nos preocupar com o número inteiro de lutas de cada indivíduo.

O indivíduo mais apto para nós, é aquele que mais vence lutas.

## Seleção

Tendo então uma medida de aptidão de cada indivíduo, devemos então ter uma forma de selecionar aqueles que se mostraram mais aptos para resolver nosso problema. No nosso caso, como dissemos antes, vamos utilizar o número de vitórias de cada indivíduo.

Esse valor pode ser utilizado de diferentes formas. Por exemplo atribuindo uma porcentagem de chance de ser selecionado proporcional a quantidade de vitórias que o indíviduo teve, e então sorteando os indidíviduos que vão passar para a próxima fase. Mas nós vamos utilizar um método mais simples, vamos simplesmente passar a metade dos indivíduos com mais vitórias.

## Cruzamento

Para nossa próxima geração, precisamos então repopular nosso mundo, já que selecionamos apenas metade da nossa população anterior. Fazemos isso cruzando nossos indivíduos selecionados.

Na prática, isso significa criar novos indivíduos em que as características dele seja parte de um dos pais e parte de outro. Nós vamos utilizar um método simples: vamos pegar metade de um dos pais e metade de outro. Exatamente quais dos atributos vai ser herdado de cada, e quem será os pais, será aleatório.

Vamos realizar cruzamentos até que tenhamos nossa população anterior.

### Mutação

E por fim, para garantir uma diversidade ao longo de nossas gerações, contamos uma pequena probabilidade de que ocorra mutação durante o cruzamento. Para nós isso significa aumentar algum atributo aleatório em 1, e diminuir outro também em 1.

## Resultado

O final de um algoritmo genético pode ser estipulado sob diferentes critérios, entre os principais podemos citar: quando atingir uma geração definida, ou quando algum indivíduo atingir um valor de aptidão estipulado. No nosso caso vamos rodar nosso código até atingir uma certa geração.

Por fim, se nossa intenção era analisar a distribuição de 100 pontos de atributos, tivemos um tivemos um erro teorico  em nosso projeto. Quando os pais geram um descendente, não há limites para a distribuição de pontos. Isso faz com que, enquanto a primeira geração tinha 100 pontos distribuidos em 4 atributos, a geração seguinte pode ter mais que isso.


Como consequência, geramos descedentes mais fortes que os pais, acima das nossas regras iniciais. Então vamos adicionar uma limitação, se os atributos de um indivíduo ultrapassar 100, perde a luta, se dos dois ultrapassar, ganha quem ficou mais próximo do 100.

Rodando nosso código, obtivemos os seguintes valores para o indivíduo com o maior nível de aptidão da última geração:

- Força: 46
- Constituição: 36
- Agilidade:  18
- Destreza:  0

E testando contra 1000 inimigos aleatórios obtivemos uma taxa de 89.0% de vitória.
