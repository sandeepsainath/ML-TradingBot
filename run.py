"""
The actual bot.
"""
from account import Account
from trade_log import TradeLog as tl


trade_log = tl('trial1')
acnt = Account(1000, trade_log)
