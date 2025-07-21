import json

import requests

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
prices = response.json()


for coin, price in prices.items():
    print(f"BTC price is ${price['usd']:,.2f}")