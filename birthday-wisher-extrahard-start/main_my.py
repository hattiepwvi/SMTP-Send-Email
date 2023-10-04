##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import os
import smtplib

my_email = "xxx@gmail.com"
password = "xxx"

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

for index, row in data.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        email = row["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
folder_path = "letter_templates"
txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
random_file = random.choice(txt_files)
with open(f"letter_templates/{random_file}") as file:
    content = file.read()
    new_content = content.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=f"Subject: Happy birthday\n\n{new_content}",
    )
