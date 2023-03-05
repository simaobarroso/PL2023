<h1>TPC3: Processador de Pessoas listadas nos Róis de Confessados</h1>

<h2>MELHORAR ISTO (TUGA) + REVER TPC</h2>

<p>O enunciado deste exercicio esta disponivel no ficheiro <a href="https://www.youtube.com/watch?v=yKQ_sQKBASM">PL2023_TPCs.ipynb</a></p>

<p>O problema comecou em como representar a informacao do processos.txt. Optei por representar numa lista de dicionarios. Cada linha do processos.txt correspondia a um dicionario.</p>
<p>Cada dicionario tinha 6 <i>keys</i> e 6 <i>values</i>. Foram utilizadas expressoes regulares bem como as funcoes aprendidas na aula para fazer isso (lembrar os nomes dos < P NOME >). E` lida cada linha do ficheiro e utilizando o modulo re e groupdict poe-se num dicionario e adiciona se a lista. Para fazer verificacao das linhas repetidas, para alem de se adicionar os criterios ao dicionario, tambem se acrescenta a um set o nome da pessoa e da mae. Isto permite chegar a um resultado final que e` uma lista de dicionarios</>
<p>Existem duas funcoes print table para fazer a printagem</p>

<h3>Exercicio 1</h3>
Para a resolucao de exercicio utilizo a criacao de uma dicionario res. As chaves deste dicionario sao os anos e os values a frequencia. Recebe como argumento a lista de dicionarios, que a vai percorrer e preencher o dicionario res, o qual da return. Para preencher o dicionario res, verifico cada elemento da lista de dicionario e vou buscar o ano. Se ja estiver no dionario essa key acrescento por um o valor la posto, caso contrario crio a chave com valor 1.

<h3>Exercicio 2</h3>

<h3>Exercicio 3</h3>

<h3>Exercicio 4</h3>

<p><b>python tpc3.py</b></p>
