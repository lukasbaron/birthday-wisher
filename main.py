##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import pandas
import random
import smtplib
import datetime as dt

now = dt.datetime.now()
actual_month = now.month
actual_day = now.day
random_text = random.choice(os.listdir("letter_templates/"))

text = open(f"letter_templates/{random_text}", "r").read()


df = pandas.read_csv("birthdays.csv")
text_dict = df.to_dict(orient="records")
for key in text_dict:
    if key["month"] == actual_month and key["day"] == actual_day:
        sending_text = text.replace("[NAME]", key["name"])
        email = "lukaspokus7@gmail.com"
        password = "asdf12345."
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="lukaspokus7@yahoo.com",
            msg=f"Subject: Happy birthday\n\n {sending_text}"
        )
        connection.close()



