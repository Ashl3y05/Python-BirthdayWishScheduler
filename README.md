﻿# Python - Birthday Wish Scheduler
A python program that will automatically sends a birthday wish to someone on their birthday

# How to use
 - Edit the birthdays.csv file to add someone with their name, email, year, month, and day of their bday
 - open the main.py and edit the following:
   - sender_email to your email
   - sender_pass to your email's password or app pasword if your email provider required a seperate pass to use for custom apps(like gmail.com)
   - smtp_address that your email provider uses(known smtp address is included in the main.py as a comment)
 - best used in the Cloud

# How to run
1. Make sure to have Python and Git installed
2. Make a folder somewhere on your pc
3. Right-click inside the folder and open in terminal
4. On the terminal type the following:
     - git clone https://github.com/Ashl3y05/Python-BirthdayWishScheduler
     - cd .\Python-BirthdayWishScheduler\
     - python main.py

# What I Learned
 - smtplib
    - smtp addresses
    - starttls
    - login
    - sendmail
 - datetime class
    - now()
    - datetime.month
    - datetime.day
  
