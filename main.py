import json
from datetime import timedelta
from os import closerange

import requests
import csv
import datetime as dt

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
prices = response.json()

# Parse the ethereum price for use
for coin, price in prices.items():
    eth_price = price['usd']

# Current time
__curr_time = dt.datetime.now()


def log_price(time_stamp: object, price: float) -> None:
    """
    Appends the current crypto price to a row in the prices csv file

    Args:
        time_stamp (obj): record of the price at this particular moment in time
        price (float): how much the crypto coin is being traded for

    Returns:
        None

    """

    formatted_time = time_stamp.strftime("%Y-%m-%dT%H:%M:%S")
    coin_price = [formatted_time, price]

    with open("price.csv", "a", newline="") as price_file:
        price_writer = csv.writer(price_file)
        price_writer.writerow(coin_price)



def signal_call(curr_time: dt.datetime) -> None:
    """
    Calculates the difference between the current price and yesterdays price (24 hours ago).
    Prints out the percentage price change to the console

    Args:
        curr_time (datetime): datetime object represents the current time

    Returns:
        None
    """
    closest_time_stamp = None
    closest_time_diff = None
    closest_price = None

    target_time = curr_time - timedelta(hours=24)
    print(f"Current time: {curr_time}")
    print(f"Target time (24 hours ago): {target_time}")

    with open("price.csv", newline="") as price_file:
        csv_reader = csv.reader(price_file)
        next(csv_reader)  # Skip header

        for row in csv_reader:
            row_time = dt.datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S")
            time_diff = abs(row_time - target_time)

            print(f"Row time: {row_time}, Difference: {time_diff}")

            if closest_time_diff is None or time_diff < closest_time_diff:
                closest_time_diff = time_diff
                closest_time_stamp = row[0]
                closest_price = row[1]

    if closest_time_stamp:
        print(f"Closest timestamp to 24h ago: {closest_time_stamp}")
        print(f"Closest price: {closest_price}")
    else:
        print("No price data available.")





#log_price(__curr_time, eth_price)
signal_call(__curr_time)


