"""
Account class used to store liquid balance and market value of session.
The class integrates with the trade log class in order to check market value.
"""
from trade_log import Trade_Log as tl


class Account:
    def __init__(self, cash, trade_log):
        self.cash = cash
        self.market_val = 0
        self.trade_log = trade_log

    # Getters
    def available_cash(self):
        return self.cash

    def get_market_value(self):
        return self.market_val

    # Accessors
    def set_market_value(self):
        # trade_log would be an object, need to define it previously and access
        # here
        # market_val = shares owned*current price
        pass

    def update(self, amount, action):
        if action == "buy":
            self.cash -= amount
            self.set_market_value()
        if action == "sell":
            self.cash += amount
            self.set_market_value()

    # Status
    def solvent(self):
        if self.market_val + self.cash > 0:
            return True
        else:
            raise RuntimeError('Account is no longer solvent')
            return False
