# Regressão Linear com os Dados do Sicor

Este Notebook apresenta uma regressão linear com os microdados disponibilizados pelo Sicor usando algumas variáveis chave para tentar avaliar o que explica o volume de crédito tomado. 
Alguns outliers são removidos usando técnicas apresentadas no livro An Introduction to Statistical Learning. 
As estimativas para os coeficientes deram todas estatisticamente significativas ao nível de 5%. Entretanto, há indícios de que o erro dessa regressão não segue uma distribuição normal e é heteroscedástico.

|Variável|Coeficiente|p-valor|Significativo a 5%|
|---|---|---|---|
|Área <br> Financiada|2375.6845|0.000|Sim|
|Receita <br> Esperada|0.2558|0.000|Sim|
|Quantidade <br> produzida|0.0356|0.006|Sim|
|Recurso <br> Próprio|0.1252|0.046|Sim|
|Juros|2562.6629|0.000|Sim|

![imagem 1](https://github.com/jpeconomia/regressao-sicor/blob/main/cov-matrix.png)

<br>

![imagem 2](https://github.com/jpeconomia/regressao-sicor/blob/main/scatter.png)

<br>

![imagem 3](https://github.com/jpeconomia/regressao-sicor/blob/main/hists.png)

<br>
![imagem 4](https://github.com/jpeconomia/regressao-sicor/blob/main/plot.png)

<br>

[Dados](https://www.bcb.gov.br/estabilidadefinanceira/tabelas-credito-rural-proagro)

