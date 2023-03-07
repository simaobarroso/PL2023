<h1>TPC3: Processador de Pessoas listadas nos Róis de Confessados</h1>

<h2>REVER TPC</h2>

<p>O enunciado deste exercício está disponível no ficheiro <a href="https://github.com/simaobarroso/PL2023/blob/main/TPC3/PL2023_TPCs.ipynb">PL2023_TPCs.ipynb</a>.</p>

<p>O primeiro passo na resolução problema começou em decidir como representar a informação do <i>processos.txt</i>. Optei por representar numa lista de dicionarios. Cada linha do processos.txt correspondia a um dicionario.</p>
<p>Cada dicionario tinha 6 <i>keys</i> e 6 <i>values</i>. Foram utilizadas expressões regulares (para esta parte, grupos de capturas) bem como as funções aprendidas na aula para fazer isso. É lida cada linha do ficheiro e utilizando o modulo <code>re</code> e <code>groupdict</code> põe-se num dicionário e adiciona se à lista. Para fazer verificação das linhas repetidas, quando se faz um diconário com os grupos de captura, também se acrescenta a um set o nome da pessoa e da mãe. Caso já exista no set esse par, a linha é descartada (foi feito isto para diminuir o tamanho de comparações feita). No final deste processo temos uma lista de dicionários.</>
<p>É de mencionar que estão feitas duas funções para imprimir as tabelas. Estas duas funções foram feitas para melhorar a visualização dos dados. Uma hipotese também foi o uso do <i>matplotlib</i>, mas a sua utilização não iria levar a uma visualização tão diferente quanto a das tabelas. São duas porque uma é para o primeiro exercicio e as outra para os exercícios seguintes.</p>

<h3>Exercicio 1</h3>
Para a resolucao de exercicio utilizo a criacao de uma dicionario res. As chaves deste dicionario sao os anos e os values a frequencia. Recebe como argumento a lista de dicionarios, que a vai percorrer e preencher o dicionario res, o qual da return. Para preencher o dicionario res, verifico cada elemento da lista de dicionario e vou buscar o ano. Se ja estiver no dionario essa key acrescento por um o valor la posto, caso contrario crio a chave com valor 1.

<h3>Exercicio 2</h3>

<h3>Exercicio 3</h3>

<h3>Exercicio 4</h3>

<p><code>python tpc3.py</code></p>

<!-- ç ã à é á ú í ì õ -->
