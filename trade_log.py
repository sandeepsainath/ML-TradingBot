"""
Trade log class stores all trades on a CSV file and periodically updates them.
It integrates with account class in order to update market value.
"""
# from account import Account
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
        self.trade_log = pd.DataFrame(columns={
            'ticker',
            'time',
            'date',
            'action',
            'price',
            'num_shares',
            'cost_basis'})
        self.trade_log = self.trade_log[['ticker', 'time', 'date',
                                         'action', 'price', 'num_shares', 'cost_basis']]
        self.portfolio = pd.DataFrame(columns={
            'ticker',
            'num_shares',
            'current_price',
            'market_value'})
        self.portfolio = self.portfolio[['ticker', 'num_shares', 'current_price', 'market_value']]

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
            market_val = self.portfolio_to_value()
            acnt.update(cost_basis, "buy", market_val)

        if action == "sell":
            market_val = self.portfolio_to_value()
            acnt.update(cost_basis, "sell", market_val)

        self.trade_log = self.trade_log.append(pd.Series([ticker, time, date, action, price, num_shares, cost_basis], index=self.trade_log.columns),
                                               ignore_index=True)

        self.update_portfolio(ticker, num_shares)

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
            ticker_price = self.update_current_price(ticker)  # need to complete that func.
            self.portfolio = self.portfolio.append(pd.Series([ticker, num_shares, ticker_price, num_shares*ticker_price], index=self.portfolio.columns),
                                                   ignore_index=True)

        else:
            self.portfolio.set_index('ticker', inplace=True)
            self.portfolio.at[ticker, 'num_shares'] += num_shares
            self.portfolio.at[ticker, 'current_price'] = self.update_current_price(ticker)
            self.portfolio.at[ticker, 'market_value'] = num_shares*self.update_current_price(ticker)
            self.portfolio.set_index(inplace=True)

    def update_current_price(self, ticker):
        '''
        Pulls the latest price for a security from the Alpha Vantage API.

        Parameters:
            - ticker: Ticker of the security
        '''
        pass  # Pull current_price from API, update self.portfolio
        return 100

    # Accessors
    def portfolio_to_value(self):
        # for ind in df.index:
        # print(df['Name'][ind], df['Stream'][ind])
        value = 0
        for i in self.portfolio.index:
            value += self.portfolio['num_shares'][i]*self.portfolio['current_price'][i]
        return value

    # End of Run
    def save_to_csv(self):
        # Saves our trade log DataFrame to a csv file.
        self.trade_log.to_csv("{}.csv".format(self.name))
