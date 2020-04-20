from trade_log import Account
from trade_log import TradeLog as tl


trade_log = tl('test1')
acnt = Account(1000, trade_log)

trade_log.trade(acnt, 'AAPL', 1200, '04/20/2000', 'buy', 100, 10)
print(trade_log.df)
