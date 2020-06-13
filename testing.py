from account import Account
from trade_log import TradeLog as tl


trade_log = tl('test1')
acnt = Account(20001)

trade_log.trade(acnt, 'AAPL', 1200, '04/20/2000', 'buy', 100, 10)
trade_log.trade(acnt, 'MSFT', 1100, '04/21/2000', 'buy', 90, 2)
print(trade_log.trade_log)
print(trade_log.portfolio)
print(trade_log.portfolio_to_value())
trade_log.save_to_csv()
