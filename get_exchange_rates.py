#!/usr/bin/env python3

from blockchain import exchangerates

ticker = exchangerates.get_ticker()

print("BTC prices")
for k in ticker:
  print("{}, {}".format(k, ticker[k].p15min))

btc = exchangerates.to_btc('EUR', 100)

print("100 EUR = {} BTC".format(btc))
