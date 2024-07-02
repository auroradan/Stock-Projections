import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Function to fetch historical S&P 500 data and calculate yearly returns
'''
ticker = '^GSPC'  # S&P 500 index ticker
start_date = '1950-01-01'
end_date = '2023-01-01'
'''
def sp500_get_yearly_returns(ticker='^GSPC', start_date='1980-01-01', end_date=None):
    if end_date is None:
        end_date = datetime(datetime.today().year, 1, 1).strftime('%Y-%m-%d') 
               
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        
        hist.sort_index(inplace=True)
        if not isinstance(hist.index, pd.DatetimeIndex):
            hist.index = pd.to_datetime(hist.index)
        
        yearly_data = hist['Close'].resample('YE').last()
        yearly_returns = yearly_data.pct_change().dropna() * 100
        df = pd.DataFrame(yearly_returns)
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].dt.year
        years = df[['Date']]
        returns = df['Close']
        return years, returns
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame(), pd.Series()

def sp500_company_list():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    rows = table.find_all('tr')[1:]

    companies = []
    for row in rows:
        cells = row.find_all('td')
        ticker = cells[0].text.strip()
        name = cells[1].text.strip()
        companies.append((ticker, name))

    df = pd.DataFrame(companies, columns=['Ticker', 'Name'])
    df.to_csv('sp500_companies.csv', index=False)
    return df