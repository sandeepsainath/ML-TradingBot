"""
Account class used to store liquid balance and market value of session.
The class integrates with the trade log class in order to check market value.
"""
# from trade_log import TradeLog as tl


class Account:
    def __init__(self, cash):
        self.cash = cash
        self.market_val = 0
        # self.trade_log = trade_log

    # Getters
    def available_cash(self):
        return self.cash

    def get_market_value(self):
        return self.market_val

    # Accessors
    def set_market_value(self, market_value):
        # trade_log function 'portfolio_to_value' needs to be used to get
        # market value
        self.market_val = market_value
        pass

    def update(self, amount, action, market_value):
        if action == "buy":
            if self.cash - amount < 0:
                raise Exception("Account's cash balance cannot go negative")
            self.cash -= amount
            self.set_market_value(market_value)
        if action == "sell":
            self.cash += amount
            self.set_market_value(market_value)

    # Status
    def solvent(self):
        if self.market_val + self.cash > 0:
            return True
        else:
            raise RuntimeError('Account is no longer solvent')
            return False
