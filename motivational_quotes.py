import smtplib
import datetime as dt
import random

# import pandas as pd

my_email = "xxx@gmail.com"
password = "xxx"

# --------------- 1. Datetime ------------------#

now = dt.datetime.now()

weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


# ------------- 2、pick your quotes -------------- #

# data = pd.read_csv('quotes.txt', delimiter='\t')
# data_list = data.values.tolist()
# quote = random.choice(data_list)
# print(quote)

# ---------------- 3、Send Email ---------------------- #


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="xxx@outlook.com",
        msg=f"Subject:Wednesday Motivation\n\n{quote}",
    )
