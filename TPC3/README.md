<h1>TPC3: Processador de Pessoas listadas nos Róis de Confessados</h1>

<h2>REVER TPC</h2>

<p>O enunciado deste exercício está disponível no ficheiro <a href="https://github.com/simaobarroso/PL2023/blob/main/TPC3/PL2023_TPCs.ipynb">PL2023_TPCs.ipynb</a>.</p>

<p>O primeiro passo na resolução problema começou em decidir como representar a informação do <i>processos.txt</i>. Optei por representar numa lista de dicionarios. Cada linha do processos.txt correspondia a um dicionario.</p>
<p>Cada dicionario tinha 6 <i>keys</i> e 6 <i>values</i>. Foram utilizadas expressões regulares (para esta parte, grupos de capturas) bem como as funções aprendidas na aula para fazer isso. É lida cada linha do ficheiro e utilizando o modulo <code>re</code> e <code>groupdict</code> põe-se num dicionário e adiciona se à lista. Para fazer verificação das linhas repetidas, quando se faz um diconário com os grupos de captura, também se acrescenta a um set o nome da pessoa e da mãe. Caso já exista no set esse par, a linha é descartada (foi feito isto para diminuir o tamanho de comparações feita). No final deste processo temos uma lista de dicionários.</>
<p>É de mencionar que estão feitas duas funções para imprimir as tabelas. Estas duas funções foram feitas para melhorar a visualização dos dados. Uma hipotese também foi o uso do <i>matplotlib</i>, mas a sua utilização não iria levar a uma visualização tão diferente quanto a das tabelas. São duas porque uma é para o primeiro exercicio e as outra para os exercícios seguintes.</p>

<h3>Exercicio 1</h3>
Para a resolução de exercicio utilizo a criação de uma dicionário <code>res</code>. As chaves deste dicionario sao os anos e os valores(<i>values</i>) a frequência. Recebe como argumento a lista de dicionarios, vai percorrer-la e preencher o dicionario res, o qual da <code>return</code>. Para preencher o dicionario res, verifico cada elemento da lista de dicionario e vou buscar o ano. Se ja estiver no dicionário essa chave acrescento por um o valor daquela chave, caso contrário crio a chave com valor 1. É utilizado <i>regex</i> para ir buscar o ano da data.

<h3>Exercicio 2</h3>
<p>
A lógica deste exercicio é a mesma do exercicio anterior, percorremos a estrutura toda e preenchemos um dicionário. Só que neste caso são 2 dicionários, um para o primeiro nome e outro para o último. Mas cada um é um dicionário de dicionários. Primeiramente utilizo regex para pegar no ano e passo o ano para século. De seguida pego nos primeiros e nos últimos nomes. Por fim acedo ao dicionário cujo a key seja o século daquela data, aí utilizo uma função auxiliar que vai aumentar o valor cuja a chave é o nome. O top 5 de nomes é feito utilizando a função <code>top5</code> que devolve para aquele século.
</p>
<p>Assim consegue-se distinguir os primeiros e últimos nomes, uma vez que há instancias em que primeiros nomes são utilizados como últimos e vice-versa.</p>

<h3>Exercicio 3</h3>
<p>
Este exercício foi o mais difícil entre os 4 devido principalmente a como retirar as relações das observações. Decidi optar por apenas contar relações que contenham "proc." à frente, contando mesmo com os que têm documento danificado. Assim sendo depois a resolução é análogo às do outro exercicio com o preenchimento de um resultado em que a chava é a relação e o valor é o número de vezes que essa relação aparece
</p>

<h3>Exercicio 4</h3>

<p>
  Neste exercicio como tenho os dados representados numa lista de dicionários, a passagem é quase direta.
  Na função <code>main</code> mandei os 20 primeiros registos da lista para a função <code>exec4</code> que simplesmente faz um <code>json.dump</code> para o ficheiro <b>exe4.json</b>.
</p>

<h3>Para executar o programa:</h3>
<p><code>python tpc3.py</code></p>

<!-- ç ã à é á ú í ì õ Ê ê-->
