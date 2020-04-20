"""
The actual bot.
"""
from account import Account
from trade_log import TradeLog
from security import Security

import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

API_URL
API_KEY = JLF3VYO6W156F6WT

ts = TimeSeries(key=API_KEY, output_format='pandas')
data_ts, meta_ts = ts.get_intraday(symbol='ticker', interval='1min', outputsize='full')

ti = TechIndicators(key=API_KEY, output_format='pandas')
period = 60
data_ti, meta_ti = ti.get_sma(symbol='ticker', interval='1min',
                              time_period=period, series_type='close')

trade_log = TradeLog('trial1')
account = Account(1000, trade_log)
