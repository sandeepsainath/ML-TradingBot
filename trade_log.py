"""
Trade log class stores all trades on a CSV file and periodically updates them.
It integrates with account class in order to update market value.
"""
from account import Account
import pandas as pd


class TradeLog:
    def __init__(self, instance_name):
        '''
        Initializes the trade log for our trading sessions.

        Parameters:
            - instance_name: The name of our trading sessions

        Class attributes:
            - self.name: Name of our trading sessions
            - self.df: DataFrame representing our successful trades
            - self.portfolio: DataFrame representing our current portfolio
        '''
        self.name = instance_name
        self.df = pd.DataFrame(columns={
            'ticker',
            'time',
            'date',
            'action',
            'price',
            'num_shares',
            'cost_basis'})

        self.portfolio = pd.DataFrame(columns={
            'ticker',
            'num_shares',
            'current_price'})

    # Trading
    def trade(self, acnt, ticker, time, date, action, price, num_shares):
        '''
        Runs our trading session and stores executed trades in the trade log.

        Parameters:
            - self.acnt: Account that we are using to trade with
            - self.ticker: Ticker of the stock being traded
            - self.time: Time of trade
            - self.date: Date of trade
            - self.action: Whether the trade is long or short
            - self.price: Price of the trade
            - self.num_shares: Positive if bought, negative if sold
        '''
        cost_basis = price*num_shares

        if action == "buy":
            acnt.update(cost_basis, "buy")

        if action == "sell":
            acnt.update(cost_basis, "sell")

        self.df.append(pd.Series(ticker, time, date, action, price, num_shares, index=self.df.columns),
                       ignore_index=True)

        update_portfolio(ticker, num_shares)

    def update_portfolio(self, ticker, num_shares):
        '''
        Updates portfolio for a particular securtity.

        This function is called in one of two scenarios:
            1. At the end of a call to trade(), which represents the successful execution of a trade
            2. In a periodic call in run.py to update a ticker's current price.

        Parameters:
            - ticker: Ticker of the security traded
            - num_shares: Number of shares bought/sold in the trade
        '''
        if ticker not in self.portfolio['ticker'].unique():
            self.portfolio.append(pd.Series(ticker, num_shares, current_price, index=self.portfolio.columns),
                                  ignore_index=True)
        else:
            security = self.portfolio[self.portfolio['ticker'] == ticker]
            security['num_shares'] += num_shares
            pull_current_price(ticker)

    def pull_current_price(self, ticker):
        '''
        Pulls the latest price for a security from the Alpha Vantage API.

        Parameters:
            - ticker: Ticker of the security
        '''
        pass  # Pull current_price from API, update self.portfolio

    # End of Run
    def save_to_csv(self):
        '''Saves our trade log DataFrame to a csv file.'''
        self.df.to_csv("{}.csv".format(self.name))
