# Os dircursos dos presidentes do Brasil na ONU

## O projeto:

Analisar, a partir dos discursos dos presidentes na abertura da Assembleia Geral das Nações Unidas, quais os termos mais utilizados em nuvem de palavras.


## Contexto:

O Brasil é, tradicionalmente, o país que abre a Assembleia Geral das Nações Unidas todos os anos. A cada uma destas solenidades, o presidente brasileiro da ocasião profere seu discurso em virtude do contexto mundial.

Desta forma, as declarações são diferentes - algumas mais focadas no Brasil, outras em âmbito global.

Os discursos analisados abrangem as gestões, por ordem de eleição, Fernando Collor de Melo (1990-1992), Fernando Henrique Cardoso (1995-1999), Luis Inácio Lula da Silva (2003-2007), Dilma Vana Rousseff (2011-2015) e Jair Bolsonaro (2019-2022). A fonte consultada foi o site da [Biblioteca Presidência da República](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes)

Um ponto a se destacar é que os discursos analisados referem-se apenas ao primeiro ano do governo de presidentes que foram reeleitos, afim de dar o mesmo tratamento a governantes que não foram reeleitos.


## Objetivo:

Utilizar a linguagem Python e bibliotecas necessárias para extrair do site os textos dos discursos em formato *.txt* e, posteriormente, transformá-los em nuvem de palavras (descartando artigos, adjetivos, advérbios e preposições, que são desnecessárias para a criação da nuvem).


## Estrutura do repositório:

* **data:** links para os arquivos **.pdf**, **.html** e **.mp3** baixados no site da Biblioteca da Presidência da República;
* **img:** capturas de tela e gráficos do projeto;
* **code:** estrutura dos códigos em **.ipynb** e **.py** (**Jupyter Notebook** e **VSCode**;
* **english version:** a translate of **reademe.md** (.pdf).


## Linguagem utilizada:

* **Python**


## Bibliotecas:

* **Numpy**
* **PyPDF2**
* **Selenium**
* **wordcloud**
* **matplotlib.pyplot**

## Metodologia:

A busca pelos discursos teve início no site da [Biblioteca Presidência da República](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes).

O critério utilizado foi o discurso proferido por cada um dos ex-presidentes no ano do seu primeiro mandato - visto que Fernando Henrique Cardoso, Luis Inácio Lula da Silva e Dilma Rousseff foram reeleitos, diferente de Fernando Collor e Jair Bolsonaro.

<img src="/img/biblioteca_presidencia.png">

##
Após o acesso, foi realizada a busca pelos discursos. Vale ressaltar que não há uniformidade nos formatos. Color, FHC1 e Lula1 estão em formato **.pdf**; Dilma1 e Bolsonaro, em formato **.html**.

Os dois últimos, pelo fato de estarem em formato **.html**, os arquivos no formato **.txt** (necessários para se criar a nuvem de palavras) foram obtidos por "scraping", com a biblioteca **Selenium**. **OBS**: foram realizadas várias tentativas com o **Beautifull Soup**, porém, o código entrou em loop e não finalizava.

Os discursos que estavam em formatos **.pdf** foram tratados pela biblioteca **PyPDF2** e, assim, resultaram em arquivos **.txt**.


## Links para os discursos(também disponíveis na pasta **data**):

* [Collor - 24/09/1990](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/fernando-collor/discursos/1990/88.pdf/view)

* [FHC 1 - 10/11/2001](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/fernando-henrique-cardoso/discursos/2o-mandato/2001/copy_of_64.pdf/view)

* [Lula 1 - 14/09/2005](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/luiz-inacio-lula-da-silva/discursos/1o-mandato/2005/discurso-do-presidente-da-republica-luiz-inacio-lula-da-silva-na-sessao-de-abertura-da-reuniao-de-alto-nivel-da-assembleia-geral-das-nacoes-unidas-metas-do-milenio/view)

* [Dilma 1 - 21/09/2011](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/dilma-rousseff/discursos/discursos-da-presidenta/discurso-da-presidenta-da-republica-dilma-rousseff-na-abertura-do-debate-geral-da-66a-assembleia-geral-das-nacoes-unidas-nova-iorque-eua)

* [Bolsonaro - 24/09/2019](http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/bolsonaro/discursos/discurso-do-presidente-da-republica-jair-bolsonaro-durante-abertura-do-debate-geral-da-74a-sessao-da-assembleia-geral-das-nacoes-unidas-agnu-nova-iorque-eua)


##
A primeira etapa foi extrair dos arquivos originais os formatos **.txt** para, depois, produzir os códigos para a criação das nuvens de palavras.

As imagens das nuvens foram realizadas utilizando as bibliotecas **numpy** (necessária para um array da máscara de nuvem), **wordcloud** (criação da nuvem) e **matplotlib** (plotagem e visualização). Uma imagem no formato de nuvem foi baixada (formato **.png**).

Houve a necessidade de se incluir algumas palavras manualmente na linha de código "stopwords", pois verificou-se, nas primeiras plotagens, a incidência de artigos, advérbios e preposições, que atrapalhavam a mehor visualização. Bem como limitou-se a 50 o número de palavras que comporiam a nuvem.


## Resultados:

**Collor**: grande incidência de "Brasil", "internacional", "países", "economia" e "cooperação". Uma abordagem mais geral da inserção do Brasil no contexto mundial e econômico.

<img src="/img/nuvem_collor.png">

##
**FHC1**: o então presidente destacou "Estado", "globalização", "desenvolvimento", "países" e "povo" as palavras em seu discurso. Mas vale, também, ressaltar a palavra "terrorismo".

<img src="/img/nuvem_fhc1.png">

##
**Lula1**: em seu primeiro mandato, Lula destacou "República", "internacional", "fome", "Brasil", "governo" e "Metas", mostrando sua preocupação em relação às questões globais e econômicas.

<img src="/img/nuvem_lula1.png">

##
**Dilma1**: "Brasil", "mundo", "desenvolvimento", "política", "países" e "crise" foram algumas das palavras que mais sobressaíram do discurso, direcionado mais aos aspectos de interesse global. Destaque-se a palavra "mulher" no discurso.

<img src="/img/nuvem_dilma1.png">

##
**Bolsonaro**: as palavras que mais se destacaram foram "Brasil", "indígena", "governo" e "liberdade", além de "Deus" (quando referiu-se a aspectos de dúvidas quanto à ideologia de seu governo).

Mas, também pode-se notar a incidência de "socialismo", "mídia", "soberania" e "verdade" (ao abordar que sua eleição afastou o país do socialismo, tratamento que recebeu da mída e ao citar versículo bíblico sobre a "verdade" - João 8:32).

<img src="/img/nuvem_bolsonaro.png">


## Análise:

O discurso de abertura da Assembleia Geral da ONU é um momento de grande importância para o Brasil. Tradicionalmente, é o país que abre os trabalhos. E é a apresentação das diretrizes que o Brasil deve tomar durante os respectivos governos. Verifica-se que alguns buscam uma abordagem mais geral e condizente e alinhado com o pensamento dos demais países-membros.

Em outros momentos, ressaltar a soberania nacional, ideologia política e econômica.
