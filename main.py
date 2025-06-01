import smtplib
import datetime as dt
import pandas as pd
import random

# You may want to edit the csv file first

sender_email = "[YOUR EMAIL]"
sender_pass = "[YOUR APP PASSWORD]"
smtp_address = "[YOUR EMAIL PROVIDER'S SMTP ADDRESS]"

# SMTP ADDRESSES
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

recipient = ""
celebrant = ""
date_now = dt.datetime.now()
month_now = date_now.month
day_now = date_now.day

birth_data = pd.read_csv("birthdays.csv")
birth_data_dict = birth_data.to_dict(orient="records")

for data in range(0, len(birth_data_dict)):
    if birth_data_dict[data]["month"] == month_now and birth_data_dict[data]["day"] == day_now:
        celebrant = birth_data_dict[data]["name"]
        recipient = birth_data_dict[data]["email"]

random_letter = f"./letter_templates/letter_{random.randint(1,3)}.txt"
with open(random_letter) as chosen_letter:
    message = chosen_letter.read()
    edited_message = message.replace("[NAME]", celebrant)

with smtplib.SMTP(smtp_address) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_pass)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=recipient,
        msg=f"Subject:Happy Birthday!\n\n{edited_message}"
    )




