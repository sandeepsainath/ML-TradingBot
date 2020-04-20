"""
The actual bot.
"""
from account import Account
from trade_log import Trade_Log as tl
import requests

trade_log = tl('trial1')
acnt = Account(1000, trade_log)

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
