<h1>TPC2: Somador on/off</h1>

<p>O enunciado deste exercicio está no ficheiro <a href="https://github.com/simaobarroso/PL2023/blob/main/TPC2/PL2023_TPC1-TPC2.ipynb">PL2023_TPC1-TPC2.ipynb</a></p>

<p>Na minha resolução, primeiro divido o texto lido (quer do terminal ou do ficheiro) por linhas. Cada linha é de seguida dividida por espaços utilizando a função <b>split</b> do prelude do python.
A função <b>trata</b> vai tratar de cada elemento do array gerando pela função <b>split</b>.</p>

<p>A opção de onde se quer que se leia o texto é escolhido no inicio da execução do programa.</p>

<p>A resolução do problema é apoiada pela utilização de duas variáveis globais. Uma para o resultado e outra para o modo (on e off).</p>

<p>Relativamente à função trata, o primeiro que faz é pegar na string e ver se tem on ou off (quer seja em maiusculas, minusculas, qualquer combinação e até no meio de outras palavras).
De seguida vai analisar a string e dependendo do modo vai adicionar as sequencias de caracteres. Por exemplo, "55a5" no programa é considerado como 55+5 (caso o modo esteja on, se for off ignora tudo)
</p>

<p>Para executar o programa basta: <b>python tpc.py</b></p>
