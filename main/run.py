"""
The actual bot.
"""
from account import Account
from trade_log import TradeLog
from security import Security
from api_calls import pull_data_time_series, pull_data_technical_indicators
from strategy import Strategy

# Create account with some balance
balance = 10000
acnt = Account(balance)
log = TradeLog('test2')

# Insert tickers to be traded
tickers = ['PEE']

# (Set/pick trading strategy)

# - technical indicator combination (portfolio)
strategy = f()

# Run bot for set amount of iterations (# of simulations)
iterations = 1

for i in range(iterations):
    for ticker in tickers:
        function = strategy.get_function()  # Daily/weekly, adjusted/non-adjusted
        interval = strategy.get_interval()  # 1min, 5min, 15min, 30min...

        # Pull time series data for relevant tickers using api_calls.py
        time_series = pull_data_time_series(function, ticker, interval)
        # Pull technical indicators data for relevant portfolio using api_calls.py
        tech_indicators = pull_data_technical_indicators()

        decision = strategy.make_decision(time_series, tech_indicators)  # 'buy' or 'sell'
        # - risk management
        # - how much of balance to be traded
        # - stop-loss order
        # - number of trades
        # - limit order
        # Make trade
        # Update trade log
