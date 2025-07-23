from datetime import timedelta
import requests
import csv
import datetime as dt
import time
from plyer import notification

try:
    while True:

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



        def price_signal(curr_time: dt.datetime, curr_price: float) -> None:
            """
            Calculates the difference between the current price and yesterday's price (24 hours ago).
            Prints out a signal to the console if the price has dropped to a certain percentage

            Args:
                curr_time (datetime): datetime object represents the current time
                curr_price (float): the current price that 1 ethereum is worth

            Returns:
                None
            """
            closest_time_stamp = None
            closest_time_diff = None
            closest_price = None

            target_time = curr_time - timedelta(hours=24)

            with open("price.csv", newline="") as price_file:
                csv_reader = csv.reader(price_file)
                next(csv_reader)  # Skip header

                for row in csv_reader:
                    row_time = dt.datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S")
                    time_diff = abs(row_time - target_time)

                    if closest_time_diff is None or time_diff < closest_time_diff:
                        closest_time_diff = time_diff
                        closest_time_stamp = row[0]
                        closest_price = row[1]

            old_price = closest_price

            old_price = float(old_price)
            percent_change = ((curr_price - old_price) / old_price) * 100
            displayed_percent_change = abs(percent_change)  # Removes the negative sign from the percentage drop message
            displayed_percent_change = format(displayed_percent_change, ".1f")  # Don't need the output to display decimals past the tenths place

            if percent_change <= -1:
                notification.notify(title="BUY SIGNAL", message=f"Ether price dropped more than {displayed_percent_change}% in 24 hours")

            elif percent_change <= -20:
                notification.notify(title="CRASH", message=f"Ether price cratered by {displayed_percent_change}% in 24 hours")

        log_price(__curr_time, eth_price)
        price_signal(__curr_time, eth_price)
        time.sleep(600) #Price logged and difference calculated at 10 minute intervals

except KeyboardInterrupt:
    print("\n Program terminated by user.")

