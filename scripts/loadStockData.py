from datetime import datetime
#import pandas as pd
import pandas_datareader as pdr
import yfinance as yf

# Hint: Start this program from the directory, where data-directory is located

start_date = "2005-01-01"
#start_date = "2019-01-01"
end_date = "2024-01-01"
load_prices = True
load_rates = True

# Define the stock ticker symbol
tickerSymbol = "MSFT"
tickerSP500 = "^GSPC"
tickerGold = "GLD"
#DATA_PATH = "data/stocks/5-years/"
DATA_PATH = "data/stocks/19-years/"
DATA_PATH_STOCK = DATA_PATH  + tickerSymbol + ".csv"
DATA_PATH_SP500 = DATA_PATH  + "SP500" + ".csv"
DATA_PATH_GOLD = DATA_PATH  + "GOLD" + ".csv"
DATA_PATH_INTEREST_RATE = DATA_PATH + "ITR" + ".csv"
DATA_PATH_CONS_PRICE_IDX = DATA_PATH + "CPI" + ".csv"
DATA_PATH_FRED_RATES = DATA_PATH + "CPI" + "-" + "FED" + ".csv"
DATA_PATH_GDP = DATA_PATH + "GDP" + ".csv"

if load_prices == True:
    # Get the historical prices for this ticker
    tickerDataStock = yf.Ticker(tickerSymbol)
    tickerDataSP500 = yf.Ticker(tickerSP500)
    tickerDataGold = yf.Ticker(tickerGold)

    # Set the period: max, 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, or custom dates
    # For custom dates, use tickerData.history(start="YYYY-MM-DD", end="YYYY-MM-DD")
    # tickerDfStock = tickerDataStock.history(period=time_period)  # Here, we're using a period of 5 years
    # tickerDfSP500 = tickerDataSP500.history(period=time_period)  # Here, we're using a period of 5 years
    # tickerDfGold = tickerDataGold.history(period=time_period)  # Here, we're using a period of 5 years
    tickerDfStock = tickerDataStock.history(start=start_date, end=end_date)
    tickerDfSP500 = tickerDataSP500.history( start=start_date, end=end_date)
    tickerDfGold = tickerDataGold.history( start=start_date, end=end_date)

    # Show the data
    # print(tickerDf)

    # write data to csv file
    print("vor to_csv")
    tickerDfStock.to_csv(DATA_PATH_STOCK)
    tickerDfSP500.to_csv(DATA_PATH_SP500)
    tickerDfGold.to_csv(DATA_PATH_GOLD)
    print("nach to_csv")

if load_rates == True:
    # read interest rates

    # Define start and end dates
    format_str = "%Y-%m-%d"
    start = datetime.strptime(start_date, format_str)
    end = datetime.strptime(end_date, format_str)

    # Download Federal Funds Effective Rate as an example
    # list = ("FEDFUNDS", "CPIAUCSL", "GDP")
    list = ("FEDFUNDS", "CPIAUCSL")
    fed_funds_rate = pdr.get_data_fred(list, start, end)
    fed_funds_gdp = pdr.get_data_fred("GDP", start, end)

    print(fed_funds_rate.head())
    print(fed_funds_rate.tail())
    # print(cpi.head())
    # print(cpi.tail())

    fed_funds_rate.to_csv(DATA_PATH_FRED_RATES)
    fed_funds_gdp.to_csv(DATA_PATH_GDP)
    # cpi.to_csv(DATA_PATH_CONS_PRICE_IDX)
