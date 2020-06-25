import requests
import pandas as pd

API_URL = "https://www.alphavantage.co/query"
API_KEY = "JLF3VYO6W156F6WT"

time_series_functions = {
    'TIME_SERIES_INTRADAY': 'Time Series',
    'TIME_SERIES_DAILY': 'Time Series (Daily)',
    'TIME_SERIES_DAILY_ADJUSTED': 'Time Series (Daily)',
    'TIME_SERIES_WEEKLY': 'Weekly Time Series',
    'TIME_SERIES_WEEKLY_ADJUSTED': 'Weekly Adjusted Time Series',
    'TIME_SERIES_MONTHLY': 'Monthly Time Series',
    'TIME_SERIES_MONTHLY_ADJUSTED': 'Monthly Adjusted Time Series',
    'GLOBAL_QUOTE': 'Global Quote',
}

def pull_data_time_series(function, symbol, interval=None, output_size="full", data_type="json"):
    '''
    Pull a security's time series data from the Alpha Vantage API.

    Parameters:
        - function: Type of time series data pulled in. Corresponds to keys in time_series_functions.
        - symbol: Ticker of the security.
        - interval: Interval for intraday time series data. Can choose between '1min', '5min', '15min', '30min', and '60min'.
        - output_size: Size of time series outputted. Can choose between "full" and "compact" (returns only the latest 100 data points).
        - data_type: Type of data output. Can choose between "json" and "csv".
    '''

    if interval == None:
        if function in ['TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED']:
            data = {"function": function,
                    "symbol": symbol,
                    "outputsize": output_size,
                    "datatype": data_type,
                    "apikey": API_KEY}
        else:
            data = {"function": function,
                    "symbol": symbol,
                    "datatype": data_type,
                    "apikey": API_KEY}

    else:
        data = {"function": function,
                "symbol": symbol,
                "interval": interval,
                "outputsize": output_size,
                "datatype": data_type,
                "apikey": API_KEY}

    response = requests.get(API_URL, data)
    response_json = response.json()

    if function = 'TIME_SERIES_INTRADAY':
        header = time_series_functions[function] + ' ({})'.format(interval)

    else:
        header = time_series_functions[function]

    data = pd.DataFrame.from_dict(
        response_json[header], orient='index').sort_index(axis=1)

    #data.index = data.index.astype('datetime')

    return data
