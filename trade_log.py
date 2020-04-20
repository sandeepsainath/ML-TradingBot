"""
Trade log class stores all trades on a CSV file and periodically updates them.
It integrates with account class in order to update market value.
"""
import account


class Trade_Log:
    def __init__(self, instance_name):
        self.name = instance_name
        # initiate CSV file with name of instance
        pass

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
        pass
