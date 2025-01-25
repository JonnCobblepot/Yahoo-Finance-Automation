
#? Importa a biblioteca yfinance
import yfinance as yf


#! Função para obter o preço atual de determinada ação
def get_stock_price(ticker):

    try:
        # Baixa os dados do 'ticker' usando a API do yfinance
        stock = yf.Ticker(ticker)
        current_price = stock.info['currentPrice']  # Obtém o preço atual da ação 'ticker'
        return current_price
    
    except Exception as e:
        print(f"Erro ao obter dados para {ticker}: {e}")
        return None
    

#! Função para obter o o histórico de preços de determinada ação definindo o período de busca
def get_historical_data(ticker, start_date, end_date):

    try:
        # Baixa os dados do 'ticker' usando a API do yfinance
        stock = yf.Ticker(ticker)

        # Baixa o histórico dos preços entre duas datas
        history = stock.history(start=start_date, end=end_date)
        return history
    
    except Exception as e:
        print(f"Erro ao obter histórico de preços para {ticker}: {e}")
        return None


#? Execução do código
if __name__ == "__main__":

    # Definindo os argumentos de teste
    ticker = "MSFT"             # Exemplo do ticker: Apple
    start_date = "2025-01-01"   # Início da busca ao histórico de preços do ticker
    end_date = "2025-01-20"     # Fim da busca ao histórico de preços do ticker


    # Chamando as funções
    price = get_stock_price(ticker)
    historical_data = get_historical_data(ticker, start_date, end_date)


    # Condicionais
    if price:
        # Se conseguiu extrair o preço, exibe o preço atual
        print(f"O preço atual da ação {ticker} é: ${price}")
    else:
        # Se não conseguiu realizar a operação, já o identifica
        print(f"Não foi possível obter o preço para {ticker}.")

    if historical_data is not None:
        # Se conseguiu extrair o histórico de preços, exibe-o
        print(f"Histórico de preços para {ticker}:\n{historical_data}")
    else:
        # Se não conseguiu realizar a operação, há este aviso
        print(f"Não foi possível obter o histórico para {ticker}.")