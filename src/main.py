
#? Importa as bibliotecas
import yfinance as yf
import polars as pl
import os


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


#! Função para ler os dados de entrada do arquivo XLSX (Planilha - Linhas e Colunas)
def read_input_file(file_path):

    try:
        # Lê o arquivo XLSX (Excel), vendo as colunas e as linhas de referência
        df = pl.read_excel(file_path)
        return df.to_dicts() # Aqui separa em dicionários para cada ticker o que será pedido nas colunas de dados
    
    except Exception as e:
        print(f"Erro ao ler o arquivo de entrada: {e}")
        return []


#! Função para salvar os dados no arquivo de saída
def save_to_output_file(data, file_path):

    try:
        # Atribui os dados obtidos pelo yfinance em tempo real sobre as ações
        df = pl.DataFrame(data)
        df.write_excel(file_path) # Escreve no arquivo, atualizando-o com as informações
        print(f"Arquivo salvo com sucesso em {file_path}")

    except Exception as e:
        print(f"Erro ao salvar o arquivo de saída: {e}")


#! Função principal que processa os dados montando as colunas
def process_data(input_file, output_file):

    # Chama a função para ler o arquivo de entrada input.xlsx que está na pasta data
    input_data = read_input_file(input_file)
    output_data = []

    # O arquivo de entrada possui as ações que se quer saber e o período de busca
    for row in input_data:
        ticker = row["Ticker"]
        start_date = row["Start Date"]
        end_date = row["End Date"]

        # Obtém o preço atual para adicionar no arquivo de saída
        current_price = get_stock_price(ticker)

        # Obtém o histórico de preços para adicionar ao arquivo de saída
        history = get_historical_data(ticker, start_date, end_date)

        # Dentro do histórico há muitas informações, sendo divididas em colunas, formando aqui a planilha
        if history is not None:
            for date, record in history.iterrows():
                output_data.append({
                    "Ticker": ticker,
                    "Preço Atual": current_price if date == history.index[0] else "",
                    "Date": date.strftime('%Y-%m-%d'),
                    "Open": record.get('Open', None),
                    "High": record.get('High', None),
                    "Low": record.get('Low', None),
                    "Close": record.get('Close', None),
                    "Volume": record.get('Volume', None),
                    "Dividends": record.get('Dividends', None),
                    "Stock Splits": record.get('Stock Splits', None)
                })

    # Salva os dados no arquivo de saída criando-o dentro da pasta data
    save_to_output_file(output_data, output_file)


#? Execução do código
if __name__ == "__main__":

    # Definindo os caminhos relativos para os arquivos dentro da pasta data
    base_dir = os.path.join(os.getcwd(), "data")
    input_file = os.path.join(base_dir, "input.xlsx")   # Arquivo de entrada na pasta data
    output_file = os.path.join(base_dir, "output.xlsx") # Arquivo de saída na pasta data

    # Processa os dados
    process_data(input_file, output_file)