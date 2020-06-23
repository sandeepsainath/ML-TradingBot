"""
Securities class is used to store ownership status, buy or sell status, and
data pulled from Vantage API for each security.
"""

import pandas as pd


class Security:
    def __init__(self, ticker):
        '''
        Initializes a Security object.

        Parameters:
            - ticker: Ticker of the security.

        Class attributes:
            - self.ownership: Whether this security is currently owned or not.
            - self.status: Whether this security has been bought or sold.
            - self.data: DataFrame containing security price data.
        '''

        self.ownership = False
        self.status = None
        self.data = pd.DataFrame(columns={'Open',
                                          'High',
                                          'Low',
                                          'Close',
                                          'AdjClose',
                                          'Volume'})
        self.data = self.data[['Open',
                               'High',
                               'Low',
                               'Close',
                               'AdjClose',
                               'Volume']]

    def get_ownership(self):
        '''Returns the ownership of the security.'''
        return self.ownership

    def get_status(self):
        '''Returns the status of the security.'''
        return self.status

    def get_data(self):
        '''Returns the price data of the security.'''
        return self.data

    def set_ownership(self, x):
        '''Sets the ownership of the security.'''
        if x:
            self.ownership = True
        elif x == False:
            self.ownership = False
        else:
            raise Exception("Did not pass boolean to function 'set_ownership'")

    def set_status(self, status):
        '''Sets the ownership of the security.'''
        self.status = status

    def set_data(self, df):
        '''Sets the price data of the security.'''
        self.data = df
        # assumes that a DataFrame containing security data is provided
