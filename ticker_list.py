import pandas as pd
import requests
import json
import time
import csv

# Capitalization minimum threshold values
MEGA_CAP = 200*(10**3) # 200 B
LARGE_CAP = 10*(10**3) # 10 B
MID_CAP = 2*(10**3) # 2 B
SMALL_CAP = 300 # 300 M
MICRO_CAP = 50 # 50 M

# Ticker lists
tickers_NASDAQ = pd.read_csv('NASDAQ.csv')['Symbol']
tickers_NYSE = pd.read_csv('NYSE.csv')['Symbol']
tickers_AMEX = pd.read_csv('AMEX.csv')['Symbol']

# Contains each API call's info
main_dict = {}

for ticker_list in [tickers_NYSE, tickers_AMEX]: # tickers_NASDAQ already processed
    for ticker in ticker_list:
        for i in range(60): # 60 tries, 1 second between, ensures we get earliest available API call
            r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol={}&token=brn4ofnrh5r8ci141v0g'.format(ticker))
            try:
                data = r.json()
                break
            except json.decoder.JSONDecodeError:
                time.sleep(1)

        # If API error or ticker info not present in API
        if not data or data == {}:
            continue

        main_dict[ticker] = data

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

with open('TOTAL_US_STOCK_MARKET.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    columns = ["ticker", "name", "finnhubIndustry", "country",  "currency", "exchange", "ipo",
               "marketCapitalization", "marketCapClass", "shareOutstanding"]
    writer.writerow(columns)

    for ticker in main_dict:
       output = [main_dict[ticker][col] for col in columns]
       writer.writerow(output)
