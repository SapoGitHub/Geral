# Projeto Difuso

## Entradas e Saídas

As entradas são a quantidade de comida e a quantidade de colonos com fome e a saída é o nível de prioridade definido para a máquina de produção de alimento.

### Estoque
Por economia de energia, é conveniente manter apenas um reservatório de comida refrigerado, então nossa quantidade de comida vai ser de 0 a 100, correspondendo a vazio e cheio equivalentemente. E vamos definir como:
- Vazio: Máximo (1) quando a quantidade é 0 e mínima (0) quando a quantidade é 50, daí em diante se mantém como 0;
- Médio: Mínimo (0) quando a quantidade é 0, máximo (1) quando a quantidade é 50, e então decai para o mínimo (0) novamente com a comida em 100;
- Cheio: Mínimo (0) desde quando a quantidade é 0 até 50, então máximo (1) quando a quantidade é 100;

![Estoque](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/estoque.png)

### Famintos
Mantenho um máximo de 10 colonos ao mesmo tempo em cada colônio, acredito que esse é um número suficiente para manter todas atividades em operação, então vamos definir a quantidade de colonos famintos como:
- Poucos: Máximo (1) quando a quantidade é 0 e mínima (0) quando a quantidade é 5, daí em diante se mantém como 0;
- Médio: Mínimo (0) quando a quantidade é 0, máximo (1) quando a quantidade é 5, e então decai para o mínimo (0) novamente quando a quantidade de colonos famintos é 10;
- Muitos: Mínimo (0) desde quando a quantidade é 0 até 5, então máximo (1) quando a quantidade é 10;

![Colonos](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/colonos.png)

### Prioridade
A prioridade no jogo é definido em uma escala de níveis entre 1 e 9, vamos classificar como:
- Baixa: Máximo (1) quando o nível é 1 e mínima (0) quando a quantidade é 5, daí em diante se mantém como 0;
- Média: Mínimo (0) quando o nível é 1, máximo (1) quando o nível é 5, e então decai para o mínimo (0) novamente quando o nível de prioridade é 9;
- Alta: Mínimo (0) desde quando o nível é 1 até 5, então máximo (1) quando a quantidade é 9;

![Colonos](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/prioridade.png)
  
## Regras Difusas
Vamos definir relações difusas entre as entradas e saídas:
- Se o estoque é vazio OU os famintos são muitos, então a prioridade é alta;
- Se o estoque é medio então a prioridade é média;
- Se o Estoque é cheio OU os famintos são poucos, então a prioridade é baixa.
  
### Aplicação das regras
Para nosso caso de teste, vamos considerar como entrada:
- Nível do estoque: 75%
- Quantidade de famintos: 7

Então dos nosso gráficos, vamos ter os seguintes grau de pertencimento a cada uma das variáveis:
Para o nível do estoque:
- Estoque vazio: 0.0
- Estoque médio: 0.5
- Estoque cheio: 0.5

E para a quantidade de colonos famintos:
- Poucos famintos: 0.0
- Medios famintos: 0.6
- Muitos famintos: 0.4


Então, para aplicar as regras, primeiro precisamos saber com quais valores vamos trabalhar.
Para a primeira regra (e a terceira), temos um OU, o que significa que devemos então pegar o valor mais alto. A primeira regra aborda estoque vazio (0.0) e muitos famintos (0.4), pegando o valor mais alto, temos para a primeira regra 0.4. A terceira regra é análoga entre estoque cheio (0.5) e poucos famintos (0.0), e nossa segunda regra pegamos o valor direto do estoque médio (0.5). Então resumidamente temos:

- Primeira regra: 0.4
- Segunda regra: 0.5
- Terceira regra: 0.5

Nosso próximo passo é ligar efetivamente as regras a nossa saída. Fazemos isso "cortando" os valores acima dos obtidos a cada regra. Por exemplo, para o nível de prioridade baixo, temos a terceira regra, então cortamos os valores em 0.5

![Gráfico cortado](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/cortado.png)

## Regra da agregação
Agora então vamos combinar os resultados obtidos anteriormente para cada variável de saída, isso é feito tipicamente somando os gráficos.

![Gráfico após as somas](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/combinado.png)

## Desfuzzificação
Finalmente, nosso último passo é obter a respostsa final. Vamos usar o método do centroide, isto é, vamos calcular o centroide de nossa figura formada.
![Centroide](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Projeto%20Difuso/imagens/resultado.png)

Ficamos um resultado de 4.89, mas como só podemos aplicar valores inteiros para o nível de prioridade no Oxygen Not Included, arredondamos nosso resultado para um <b>nível de prioridade 5</b>;
