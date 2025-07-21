import json
import requests
import csv
import datetime as dt

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
prices = response.json()


for coin, price in prices.items():
    btc_price = price['usd']

# Current time
time = dt.datetime.now()


def log_price(time_stamp: object, price: float) -> None:
    """
    Appends the current crypto price to a row in the prices csv file

    Args:
        time_stamp (str): record of the price at this particular moment in time
        price (float): how much the crypto coin is being traded for

    Returns:
        None

    """

    formatted_time = time_stamp.strftime("%G-%m-%dT%H:%M:%S")
    coin_price = [formatted_time, price]

    with open("prices.csv", "a", newline="") as prices_file:
        writer = csv.writer(prices_file)
        writer.writerow(coin_price)

log_price(time, btc_price)



