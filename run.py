"""
The actual bot.
"""
import account
import trade_log as tl

trade_log = tl('trial1')
acnt = account(1000, trade_log)
