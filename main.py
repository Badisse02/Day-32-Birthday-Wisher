##################### Extra Hard Starting Project ######################
from pandas import *
from random import *
from datetime import *
from smtplib import *

# 1. Update the birthdays.csv
data = read_csv("birthdays.csv")
df = data.to_dict(orient="records")
day = datetime.now().day
month = datetime.now().month
Email = "Your Email"
password = "Your Password"
for person in df:

    # 2. Check if today matches a birthday in the birthdays.csv

    if person["month"] == month and person["day"] == day:
        # 3. If step 2 is true, pick a random letter from letter templates
        # and replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as doc:
            letter = doc.read().replace("[NAME]", person["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=Email, password=password)
            connection.sendmail(from_addr=Email,
                                to_addrs=person["email"],
                                msg=f"Subject: Happy Birthday Baby\n\n{letter} ")
