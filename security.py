"""
Securities class is used to store ownership status, buy or sell status, and
data pulled from Vantage API for each security.
"""

import pandas as pd


class Security:
    def __init__(self, ticker):
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
        # Create Stock Price History DataFrame

    # Getters
    def get_own(self):
        return self.ownership

    def get_status(self):
        return self.status

    def get_data(self):
        return self.data

    # Setters
    def set_ownership(self, x):
        if x == True:
            self.ownership = True
        elif x == False:
            self.ownership = False
        else:
            raise Exception("Did not pass boolean to function 'set_ownership'")

    def set_status(self, status):
        self.status = status

    def set_data(self, df):
        self.data = df
        # assumes that a DataFrame containing security data is provided
