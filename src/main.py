
#? Importa a biblioteca yfinance
import yfinance as yf

#! Função para obter o preço atual de ações
def get_stock_price(ticker):

    try:
        # Baixa os dados do 'ticker' usando a API do yfinance
        stock = yf.Ticker(ticker)
        current_price = stock.info['currentPrice']  # Obtém o preço atual da ação 'ticker'
        return current_price
    
    except Exception as e:
        print(f"Erro ao obter dados para {ticker}: {e}")
        return None

#? Execução do código
if __name__ == "__main__":
    ticker = "AAPL"  # Exemplo do ticker: Apple
    price = get_stock_price(ticker)

    if price:
        # Se conseguiu extrair o preço, exibe o preço atual
        print(f"O preço atual da ação {ticker} é: ${price}")
    else:
        # Se não conseguiu realizar a operação, já o identifica
        print(f"Não foi possível obter o preço para {ticker}.")