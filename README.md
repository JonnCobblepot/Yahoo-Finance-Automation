# Yahoo! Finance Automation

## Sobre

Este programa extrai dados do Yahoo! Finance, mais precisamente, dados de ações de empresas do mercado, as denominadas por símbolos, os tickers, por exemplo: no mercado de ações a Apple possui como abreviatura AAPL, o Google como GOOGL, a Tesla como TSLA, e por assim vai para serem identificadas na bolsa de valores. O código aqui desenvolvido consegue coletar o preço das ações em tempo real e o histórico delas ao denominar um período de busca entre duas datas. Junto com o histórico, vem também outras informações importantes para analistas do mercado, e tudo o que é extraído é inserido numa planilha Excel como arquivo de saída.

Observação: Caso não possua acesso a linguagens de programação instaladas ou compiladores ou os programas necessários e o entendimento do código, basta clicar no arquivo executável que gerará o arquivo de saída na pasta de dados (data).

---

## Objetivo

Este projeto possui como objetivo automatizar a coleta de dados da API do site de busca Yahoo! Finance. Ele simplifica e automatiza atividades repetitivas e manuais, além de proporcionar uma visualização dos dados obtidos de forma prática e mais visual, plotando-os em formato de planilha no Excel, facilitando o trabalho de analistas de dados. Com isso, este programa eliminaria uma dificuldade operacional comum: a tarefa de inserir manualmente dados de uma planilha como input para buscas em um site de informações e coletar manualmente os resultados um a um.

---

## Funcionamento

O Yahoo Finance é a fonte de dados para os preços das ações. A ideia é que o analista ou qualquer outra pessoa insira os tickers que ele deseja pesquisar na planilha de entrada, e o código desenvolvido automatize o processo de buscar os preços atualizados para esses tickers. Assim, isso não será preciso fazer manualmente.

O fluxo de entrada e saída de dados funciona da seguinte forma:

1. **Planilha de entrada (input.xlsx)**: é criada uma planilha simples no Excel que possui como colunas: Ticker, que são as as abreviaturas das ações (ex: AAPL, TSLA); Start_Date, sendo a data de início para o histórico; e o End_Date, sendo a data de término para o histórico (Esta planilha pode ser editada para seus devidos fins de interesse em diferentes tickers a serem analisados).

2. **Busca no Yahoo! Finance**: o código (main.py ou main.exe) lê essa planilha, consulta o Yahoo Finance para cada ticker e obtém os preços atualizados e o histórico das ações.

3. **Planilha de saída (output.xlsx)**: o código gera uma nova planilha com os tickers e os preços atualizados, além de demais dados destas ações. Esta planilha é o produto final que poderá ser analisada.

---

## Vídeo do Funcionamento do Programa

Fiz um vídeo mostrando o código e a execução com sucesso do código e está presente em meu canal no YouTube. Segue abaixo o link:

[https://youtu.be/ygAncffFft0](https://youtu.be/ygAncffFft0) 

---

## Vantagem de Utilização

- **Personalização**: quem estiver usando pode escolher quais tickers quer consultar, sem depender do programador.

- **Automação**: a busca dos preços e históricos das ações, os indicadores financeiros, métricas relevantes das empresas no mercado e a criação da planilha de saída no Excel formatando os dados para análise são totalmente automatizadas. Ler os dados de entrada de uma planilha Excel, que contém os códigos das empresas ou informações relevantes para busca.

- **Atualização em tempo real**: os dados vêm diretamente do Yahoo Finance, garantindo que os preços sejam os mais recentes disponíveis.

---

## Dados Extraídos plotados na Planilha de Saída do Excel (output.xlsx)

- `Ticker`: a ação a ser analisada
- `Preço atual`: independe do período de busca adicionado, mostrando em tempo real o preço da ação
- `Date`: _Data_; intervalo de tempo expresso em formato de datas (Ex 01/01/2025) no qual se obtém os dados das ações em um período
- `Open`: _Abertura_; é o preço que a ação é negociada pela 1° vez no início de um dia de mercado
- `High`: _Alta_; é o preço mais alto que a ação foi negociada durante aquele dia
- `Low`: _Baixa_; é o preço mais baixo que a ação foi negociada durante aquele dia
- `Close`: _Fechamento_; é o preço final que a ação foi negociada no fim do dia de mercado
- `Volume`: _Volume_; é o número total de ações que foram compradas e vendidas dentro de um período
- `Dividends`: _Dividendos_; são os pagamentos feitos pelas empresas aos seus acionistas, normalmente em dinheiro, vindos dos lucros da empresa
- `Stock Splits`: _Desdobramentos de Ações_; ocorre quando uma empresa divide suas ações em um número maior de ações, diminuindo o preço de cada ação individual, mas mantendo o valor total da empresa o mesmo, não o alterando

---

## Estrutura do Repositório

```{.sourceCode .bash}
Yahoo-Finance-Automation
├── data/
│   ├── input.xlsx
│   └── output.xlsx
├── src/
│   └── main.py
├── .gitattributes
├── main.exe
├── Passo a Passo.ipynb
├── README.md
├── Regras do Desafio Tecnico - Acorn.pdf
├── requirements.txt
└── Vídeo do Funcionamento do Programa.mp4
```

---

## Explicação dos Arquivos

- `Pasta data`: há os arquivos de entrada e saída, referentes às planilhas mencionadas no tópico de Funcionamento
- `Pasta src`: há o arquivo "main.py" com o código que faz toda a automação acontecer, o qual será descrito nos tópicos abaixo
- `.gitattributes`: é usado no Git para configurar como o repositório deve lidar com diferentes tipos de arquivos, e nesse caso é referente ao arquivo main.exe que é tratado pelo Git LFS (Large File Storage), por ultrapassar o limite de 100 mb
- `main.exe`: arquivo executável, basta clicar nele que o programa automaticamente rodará e gerará a planilha de saída
- `Passo a Passo.ipynb`: aqui está a descrição passo a passo do desenvolvimento deste projeto, indo passo a passo no código, no desenvolvimento do pensamento de cada etapa, as instalações das dependências e bibliotecas necessárias e minhas observações e experiências ao longo da confecção deste projeto
- `README.md`: este que você está lendo aqui agora :)
- `Regras do Desafio Tecnico - Acorn.pdf`: iniciei este projeto como desafio prático e técnico da empresa Acorn e aqui está o que foi solicitado
- `requirements.txt`: ajuda na documentação e gerenciamento de dependências
- `Vídeo do Funcionamento do Programa.mp4`: fiz um vídeo mostrando o código e a execução com sucesso do código e está presente em meu canal no YouTube, além disso também esta aqui no repositório. [Link novamente](https://youtu.be/ygAncffFft0) 

---

## Sobre o Executável main.exe

O executável é importante porque o analista de M&A geralmente não tem Python instalado no computador. Assim, com o executável, o analista só precisará clicar no .exe, que ele automaticamente irá ler o input.xlsx, processará os dados via Yahoo! Finance e gerará ou atualizará o arquivo de saída output.xlsx com os resultados, dentro da pasta data.

---

## Entendimento do Código main.py

O código main.py é composto pelas seguintes funções, funcionando da seguinte forma:

- `Ferramenta de Extração de Dados`: foi utilizado o `yfinance`, o qual é uma ferramenta de código aberto que utiliza das APIs públicas do Yahoo! Finance, e através dela é possível extrair os dados das ações e referentes ao mercado financeiro

- `Funções de Extração de Dados`: desenvolvi duas funções com esse fim: `get_stock_price(ticker)`, a qual obtém o preço atual de uma ação com base no seu ticker; e a `get_stock_history(ticker, start_date, end_date)`, a qual obtém o histórico de preços e características de uma ação entre duas datas definidas

- `Função de Leitura`: a função `read_input_file(file_path)` lê o arquivo de entrada input.xlsx que está em formato de planilha do Excel utilizando a biblioteca `Polars`. Ela retorna os valores do Ticker, Start_Date e End_Date

- `Função de Processamento dos Dados`: a função `process_data(input_file, output_file)`fornece para cada linha da planilha de entrada, os preços atuais e o histórico, os quais serão buscados e organizados para o arquivo de saída output.xslx que também está em formato de planilha do Excel

- `Função de Escrita`: a função `save_to_output_file(data, file_path)` escreve os resultados (preços atuais e históricos) na planilha de saída output.xlsx, sendo o último passo ao processar os dados

---

## Aviso Legal

<table border=1 cellpadding=10><tr><td>

#### **AVISO LEGAL IMPORTANTE**

---

**Yahoo!, Y!Finance e Yahoo! finance são marcas registradas da Yahoo, Inc.**

O yfinance é uma biblioteca desenvolvida e iniciada por Ran Aroussi, sendo fornecida no seu [GitHub](https://github.com/ranaroussi/yfinance) e que atualmente há uma comunidade que o desenvolve. Sua [Documentação](https://ranaroussi.github.io/yfinance/index.html).

O yfinance **não** é afiliado, endossado ou verificado pelo Yahoo, Inc. É uma ferramenta de código aberto que usa as APIs disponíveis publicamente do Yahoo e se destina a fins educacionais e de pesquisa.

**Você deve consultar os termos de uso do Yahoo! Os quais se encontram abaixo Para obter detalhes sobre seus direitos de usar os dados reais baixados.**

[Termos de uso da API do desenvolvedor do Yahoo](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm) 

[Termos de serviço do Yahoo](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html)

[Termos do Yahoo](https://policies.yahoo.com/us/en/yahoo/terms/index.htm) 

</td></tr></table>