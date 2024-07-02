# S&P 500 Returns Analysis and Visualization

This project analyzes and visualizes the historical returns of S&P 500 companies. It includes functions to fetch and calculate yearly returns, perform linear regression on the returns, identify top-performing companies, and automatically fetch the latest list of S&P 500 companies from Wikipedia.

## Features

- **Fetch Yearly Returns**: Retrieve and calculate yearly returns of the S&P 500 index and individual companies using `yfinance`.
- **Linear Regression Analysis**: Perform linear regression on the historical returns to predict future trends.
- **Top-Performing Companies**: Identify and plot the top-performing S&P 500 companies based on their average returns and regression slopes.
- **Automatic Data Fetching**: Automatically fetch the latest list of S&P 500 companies from Wikipedia.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/sp500-returns-analysis.git
    cd sp500-returns-analysis
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Fetch and Analyze S&P 500 Returns

1. **Analyze S&P 500 Yearly Returns**:

    ```python
    from sp500_analysis import sp500_yearly_returns_regression

    sp500_yearly_returns_regression()
    ```

2. **Identify Top-Performing S&P 500 Companies**:

    ```python
    from sp500_analysis import best_sp500_companies

    best_sp500_companies(n=5)
    ```

## Functions

### `sp500_yearly_returns_regression()`

Fetches the yearly returns of the S&P 500 index, performs linear regression, and plots the actual vs. predicted returns.

### `best_sp500_companies(n=5)`

Identifies and plots the top `n` S&P 500 companies based on their average returns and regression slopes.

### `sp500_get_yearly_returns(ticker='^GSPC', start_date='1980-01-01', end_date=None)`

Fetches historical data for a given ticker and calculates yearly returns.

### `sp500_company_list()`

Fetches the latest list of S&P 500 companies from Wikipedia.

### `get_linear_regression_model(years, returns)`

Performs linear regression on the given years and returns data.

## Dependencies

- `pandas`
- `numpy`
- `yfinance`
- `requests`
- `beautifulsoup4`
- `sklearn`
- `matplotlib`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
