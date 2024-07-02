from sp500_data import sp500_get_yearly_returns, sp500_company_list

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os.path
import heapq
import numpy as np

def sp500_yearly_returns_regression():
    years, returns = sp500_get_yearly_returns()

    model = get_linear_regression_model(years, returns)

    plt.plot(years, returns, label='Actual')
    plt.plot(years, model.predict(years), label='Predicted')
    plt.xlabel('Year')
    plt.ylabel('Return (%)')
    plt.legend()
    plt.show()

def best_sp500_companies(n=5):
    df = []
    if os.path.isfile('sp500_companies_data.csv'): 
        df = pd.read_csv('sp500_companies_data.csv')
        df['Years'] = df['Years'].apply(eval)
        df['Returns'] = df['Returns'].apply(eval)
    else:
        if os.path.isfile('sp500_companies.csv'):
            companies = pd.read_csv('sp500_companies.csv')
        else:
            companies = sp500_company_list()
        sp500_companies_data = []
        for index, row in companies.iterrows():
            ticker = row['Ticker']
            name = row['Name']
            years, returns = sp500_get_yearly_returns(ticker=ticker)
            if years.empty or returns.empty:
                continue
            model = get_linear_regression_model(years, returns)
            sp500_companies_data.append((name, list(years['Date']), list(returns), model.coef_[0], model.intercept_))
        df = pd.DataFrame(sp500_companies_data, columns=['Name', 'Years', 'Returns', 'Slope', 'Intercept'])
        df.to_csv('sp500_companies_data.csv', index=False)
    
    positive_slope_df = df[df['Slope'] >= 0]
    best_n_companies = []
    heapq.heapify(best_n_companies)
    for index, row in positive_slope_df.iterrows():
        avg_return = np.mean(row['Returns'])
        if len(best_n_companies) < n:
            heapq.heappush(best_n_companies, (avg_return, row['Name'], row['Slope'], row['Intercept'], row['Years']))
        else:
            heapq.heappushpop(best_n_companies, (avg_return, row['Name'], row['Slope'], row['Intercept'], row['Years']))
    
    fig, axis = plt.subplots(1, 2, figsize=(14, 6))  # Adjust figsize as needed
    colors = plt.cm.tab20(np.linspace(0, 1, len(best_n_companies)))
    
    for (avg_return, name, slope, intercept, years), color in zip(best_n_companies, colors):
        x = np.array(years)
        y = slope * x + intercept
        axis[0].plot(x, y, label=f'{name} (Predicted)', color=color)
        axis[1].plot(x, df[df['Name'] == name]['Returns'].values[0], label=f'{name} (Actual)', color=color)
    
    axis[0].legend()
    axis[0].set_xlabel('Year')
    axis[0].set_ylabel('Returns')
    axis[0].set_title('Predicted Returns')
    
    axis[1].legend()
    axis[1].set_xlabel('Year')
    axis[1].set_ylabel('Returns')
    axis[1].set_title('Actual Returns')
    
    plt.tight_layout()
    plt.show()

def get_linear_regression_model(years, returns):
    model = LinearRegression()
    model.fit(years.values.reshape(-1, 1), returns.values)
    return model

# Example usage
best_sp500_companies()
#sp500_yearly_returns_regression()
