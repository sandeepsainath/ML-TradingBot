"""
The actual bot.
"""
from account import Account
from trade_log import TradeLog
# from security import Security

import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

API_URL = "https://www.alphavantage.co/query"
API_KEY = "JLF3VYO6W156F6WT"

# API stuff

trade_log = TradeLog('trial1')
account = Account(1000, trade_log)

ts = TimeSeries(key=API_KEY, output_format='pandas')
data_ts, meta_ts = ts.get_intraday(symbol='ticker', interval='1min', outputsize='full')

ti = TechIndicators(key=API_KEY, output_format='pandas')
period = 60
data_ti, meta_ti = ti.get_sma(symbol='ticker', interval='1min',
                              time_period=period, series_type='close')


##############

API_URL = "https://www.alphavantage.co/query"
symbol = 'SMBL'

data = {"function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "datatype": "json",
        "apikey": "your_api_key"}

response = requests.get(API_URL, data)
response_json = response.json()  # maybe redundant

data = pd.DataFrame.from_dict(
    response_json['Time Series (Daily)'], orient='index').sort_index(axis=1)
data = data.rename(columns={'1. open': 'Open',
                            '2. high': 'High',
                            '3. low': 'Low',
                            '4. close': 'Close',
                            '5. adjusted close': 'AdjClose',
                            '6. volume': 'Volume'})
data = data[['Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']]
data.tail()  # check OK or not
