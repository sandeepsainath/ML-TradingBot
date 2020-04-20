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
            - self.name:
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
            'current_price'
        })

    # Trading
    def trade(self, acnt, ticker, time, date, action, price, num_shares):
        cost_basis = price*num_shares
        if action == "buy":
            acnt.update(cost_basis, "buy")
            pass
        if action == "sell":
            acnt.update(cost_basis, "sell")
            pass
        # store ticker, time, etc to CSV file
        self.df['ticker'] = ticker
        self.df['time'] = time
        self.df['date'] = date
        self.df['action'] = action
        self.df['price'] = price
        self.df['num_shares'] = num_shares
        self.df['cost_basis'] = cost_basis

    # End of Run

    def save_to_csv(self):
        self.df.to_csv()
