import pandas as pd
import requests
import json
import time
import csv

# Capitalization minimum threshold values
MEGA_CAP = 200*(10**9) # 200 B
LARGE_CAP = 10**9 # 10 B
MID_CAP = 2*(10**9) # 2 B
SMALL_CAP = 300*(10**6) # 300 M
MICRO_CAP = 50*(10**6) # 50 M

# Ticker lists
tickers_NASDAQ = pd.read_csv('NASDAQ.csv')['Symbol']
tickers_NYSE = pd.read_csv('NYSE.csv')['Symbol']
tickers_AMEX = pd.read_csv('AMEX.csv')['Symbol']

# Contains each API call's info
main_dict = {}

for ticker_list in tickers_NASDAQ.iloc[0:10]: #[tickers_NASDAQ, tickers_NYSE, tickers_AMEX]:
    for ticker in ticker_list:
        r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol={}&token=brn4ofnrh5r8ci141v0g'.format(ticker))
        try:
            data = r.json()
        # 60 calls/min API limit reached
        except json.decoder.JSONDecodeError:
            time.sleep(50)
            r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol={}&token=brn4ofnrh5r8ci141v0g'.format(ticker))
            data = r.json()

        main_dict[ticker] = r.json()

        # Classifying each ticker by market cap
        if main_dict[ticker]['marketCapitalization'] > MEGA_CAP:
            main_dict[ticker]['marketCapClass'] = 'MEGA_CAP'
        elif main_dict[ticker]['marketCapitalization'] > LARGE_CAP:
            main_dict[ticker]['marketCapClass'] = 'LARGE_CAP'
        elif main_dict[ticker]['marketCapitalization'] > MID_CAP:
            main_dict[ticker]['marketCapClass'] = 'MID_CAP'
        elif main_dict[ticker]['marketCapitalization'] > SMALL_CAP:
            main_dict[ticker]['marketCapClass'] = 'SMALL_CAP'
        else:
            main_dict[ticker]['marketCapClass'] = 'MICRO_CAP'

# Convert dictionary to csv
with open('TOTAL_US_STOCK_MARKET.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for ticker in main_dict:
       output = list(main_dict[ticker])
       output.insert(0, ticker) # insert ticker name at 0th element
       writer.writerow(output) # ['key', 1, 2, 3] not [['key'], [1, 2]]
