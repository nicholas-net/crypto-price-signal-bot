import json
import requests
import csv
import datetime as dt

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
prices = response.json()

# Parse the bitcoin price for use
for coin, price in prices.items():
    btc_price = price['usd']

# Current time
curr_time = dt.datetime.now()


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

    with open("prices.csv", "a", newline="") as price_file:
        price_writer = csv.writer(price_file)
        price_writer.writerow(coin_price)



def signal_call(curr_time: object, ) -> None:
    """
    Reads the csv file, finds the row with the timestamp ~24 hours ago
    Calculates the price change and prints the results

    Args:
        curr_time (obj): current local time

    Returns:
        None
    """

    with open("prices.csv", newline="") as price_file:
        time_reader = csv.reader(price_file)
        next(time_reader) # Skip column names header
        for time_stamp in time_reader:
            dt.datetime.strptime(time_stamp[0], "%Y-%m-%dT%H:%M:%S")
            print(time_stamp[0])





#log_price(curr_time, btc_price)
signal_call(curr_time)