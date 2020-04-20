"""
The actual bot.
"""
from account import Account
from trade_log import TradeLog
from security import Security

import requests
import pandas as pd


trade_log = TradeLog('trial1')
account = Account(1000, trade_log)
