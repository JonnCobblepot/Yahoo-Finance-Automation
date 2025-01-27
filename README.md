# Yahoo! Finance Automation

## Sobre

Este programa extrai dados do Yahoo! Finance, mais precisamente, dados de ações de empresas do mercado, as denominadas por símbolos, os tickers, por exemplo: no mercado de ações a Apple possui como abreviatura AAPL, o Google como GOOGL, a Tesla como TSLA, e por assim vai para serem identificadas na bolsa de valores. O código aqui desenvolvido consegue coletar o preço das ações em tempo real e o histórico delas ao denominar um período de busca entre duas datas. Junto com o histórico, vem também outras informações importantes para analistas do mercado, e tudo o que é extraído é inserido numa planilha Excel como arquivo de saída. 

Observação: Caso não possua acesso a linguagens de programação instaladas ou compiladores 

---

## Objetivo

Este projeto possui como objetivo automatizar a coleta de dados da API do site de busca Yahoo! Finance. Ele simplifica e automatiza atividades repetitivas e manuais, além de proporcionar uma visualização dos dados obtidos de forma prática e mais visual, plotando-os em formato de planilha no Excel, facilitando o trabalho de analistas de dados. Com isso, este programa eliminaria uma dificuldade operacional comum: a tarefa de inserir manualmente dados de uma planilha como input para buscas em um site de informações e coletar manualmente os resultados um a um.  

## Funcionamento

## Dados Extraídos

- `Ticker`: a ação a ser analisada
- `Preço atual`: independe do período de busca adicionado, mostrando em tempo real o preço da ação
- `Date`: *Data*; intervalo de tempo expresso em formato de datas (Ex 01/01/2025) no qual se obtém os dados das ações em um período
- `Open`: *Abertura*; é o preço que a ação é negociada pela 1° vez no início de um dia de mercado
- `High`: *Alta*; é o preço mais alto que a ação foi negociada durante aquele dia
- `Low`: *Baixa*; é o preço mais baixo que a ação foi negociada durante aquele dia
- `Close`: *Fechamento*; é o preço final que a ação foi negociada no fim do dia de mercado
- `Volume`: *Volume*; é o número total de ações que foram compradas e vendidas dentro de um período
- `Dividends`: *Dividendos*; são os pagamentos feitos pelas empresas aos seus acionistas, normalmente em dinheiro, vindos dos lucros da empresa
- `Stock Splits`: *Desdobramentos de Ações*; ocorre quando uma empresa divide suas ações em um número maior de ações, diminuindo o preço de cada ação individual, mas mantendo o valor total da empresa o mesmo, não o alterando

## Estrutura do Repositório

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
└── requirements.txt

## Explicação dos Arquivos

## Entendimento do Código

## Aviso Legal