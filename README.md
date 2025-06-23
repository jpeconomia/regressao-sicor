# Regressão Linear com os Dados do Sicor

Este Notebook apresenta uma regressão linear com os microdados disponibilizados pelo Sicor para o ano de 2024 usando algumas variáveis chave para tentar avaliar o que explica o volume de crédito tomado. Os dados são importados de forma bem desestruturada e um outro arquivo .py mostra como organizá-los para que este notebook seja reproduzível. 
Alguns outliers são removidos usando técnicas apresentadas no livro An Introduction to Statistical Learning. 
As estimativas para os coeficientes deram todas estatisticamente significativas ao nível de 5%. Entretanto, há indícios de que o erro dessa regressão não segue uma distribuição normal e é heteroscedástico.

|Variável|Coeficiente|p-valor|Significativo a 5%|
|---|---|---|---|
|Área <br> Financiada|2277.1065|0.000|Sim|
|Receita <br> Esperada|0.2549|0.000|Sim|
|Quantidade <br> produzida|0.0318|0.006|Sim|
|Recurso <br> Próprio|0.1228|0.046|Sim|
|Juros|2885.4042|0.000|Sim|

![imagem 1](https://github.com/jpeconomia/regressao-sicor/blob/main/cov-matrix.png)

<br>

![imagem 2](https://github.com/jpeconomia/regressao-sicor/blob/main/scatter.png)

<br>

![imagem 3](https://github.com/jpeconomia/regressao-sicor/blob/main/hists.png)

<br>

![imagem 4](https://github.com/jpeconomia/regressao-sicor/blob/main/plot.png)

<br>

[Dados](https://www.bcb.gov.br/estabilidadefinanceira/tabelas-credito-rural-proagro)

