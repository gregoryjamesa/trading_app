
import requests

ticker = "AAPL"
apikey = "05sToe92mVzfK42pQ2DKtRXxDeWi1nuc"
start_date = "2023-01-01"
end_date = "2023-01-31"

def get_stock_data(symbol, apikey, start_date, end_date):
    url = f"https://financialmodelingprep.com/stable/historical-price-eod/full?symbol={ticker}&apikey={apikey}&from={start_date}&to={end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_stock_data():
    data = get_stock_data(ticker, apikey, start_date, end_date)
    if data:
        for i in data:
            if i['changePercent'] > 0:
                print(i['open'])
            else:
                print("Stock went down : ()")
    else:
        print("Failed to retrieve data")

print_stock_data()