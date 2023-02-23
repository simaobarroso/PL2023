<h1>TPC1: Análise de dados: doença cardíaca</h1>

<p> O enunciado deste exercicio esta no ficheiro <b>PL2023_TPC1-TPC2.ipynb</b>, assim como o ficheiro csv utilizado para a resolucao (<b>myheart.csv</b>)</p>

<p>O primeiro passo na resolucao deste exercicio foi pensar como se iria armazenar o ficheiro csv. Como nao se podia recorrer a nenhum <i>import</i>, decidi optar por um dicionario em que a <i>key</i> é a linha do ficheiro csv e o value é um array com cada um dos parametros do csv. Isto permite uma analise mais facil do csv, uma vez, se por algum motivo(como por exemplo a idade estar como uma letra) der erro, facilmente imprimindo o dicionario ve-se a linha que falta, uma vez que a funcao <b>trata</b>, que trata de cada linha do csv, passa essa linha (e esse indice de linha) se der algum erro.
</p>
<p>O facto do values serem arrays deve-se ao facto de serem sempre um numero fixo e na mesma posicao, portanto seria <i>standard</i> o acesso e <a href= "https://www.geeksforgeeks.org/why-does-accessing-an-array-element-take-o1-time/">rapido</a>.</p>

<p>Relativamente a estrutra de dados para representar o resultado de cada distribuicao da doenca, optei novamente por um dicionario para cada tipo de distribuicao. Optei por isto ao inves de um array devido a flexibilidade de adicionar parametros (exemplo no caso do sexo) e a ser mais facil a leitura do seu significado. Outro fator nao menos importante é para me familizar melhor com este tipo de estruturas.</p>

Claro que tenho de mencionar que nao ha nenhuma estrutura de dados que fosse o <i>santo graal</i>, mas pelas razoes acima mencionadas decidi usar dicionarios.

<p>Ao longo do ficheiro de codigo, cada funcao esta explicada, para facilitar a leitura e compreensao.</p>

<p>A quando do inicio do programa ha uma interface grafica basica. é apresentada uma opcao para escolher cada distribuicao, e sao apresentadas as em modo tabela e as do matploblib ao mesmo tempo. Este tipo de tabelas ajuda-nos a retirar mais facilmente conclusoes dos dados. Por fim gostaria tambem de mencionar que visualizar os dados por percentagem tambem seria uma boa opcao, mas optei por em absoluto porque rapidamente sao retirados esses dados e o contrario é mais dificil.</p>

<p>NOTA : Decide nao retirar pessoas com niveis de colestrol a 0, uma vez que pode ser querer ser feita a analise de por exemplo quanta gente nao fez mediu o colestrol comparativamente ao resto. Supos que 0 seja o caso default da nao medicao de colestrol. Nos casos de valores extremamente elevados, mantive na mesma porque pode ser precisa uma reavaliacao, por exemplo. Como nao sabemos quem vai avaliar os dados e para que que vao avaliar, bem como o facto de o csv ser relativamente pequeno, contruibui para este pensamento que dados a mais sao melhores que dados a menos.</p>

<p>Um aspecto negativo da minha resolucao é o facto de percorrer a estrutura de dados duas vezes, uma para procurar o max e o min e outra para preencher o dicionario de resposta. Claro que isto podia ser feito de maneira mais eficiente, mas creio que devido ao dataset ser pequeno e a reutilizacao das funcao encontraMinMax para as varias distriuicoes acaba por ser uma troca de perda de perfomance por ganho de facilidade de leitura e de modularidade.</p>

<p>Para executar o programa basta : <b>python tpc1.py</b></p>

<b>Requer o MatPlotLib e python-gobject instalado</b>
