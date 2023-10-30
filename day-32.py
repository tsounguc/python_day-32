# # Simple Mail Transfer Protocol (SMTP)
# import smtplib
#
# my_email = "tsounguc@mail.gvsu.edu"
# password = ""
#
# # my_email = "christiantsoungui@gmail.com"
# # password = ""
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # Secure the connection with Transport Layer Security (TLS)
#     connection.starttls()
#     # Login to account
#     connection.login(user=my_email, password=password)
#     # Send email
#     connection.sendmail(from_addr=my_email, to_addrs="corbetke@mail.gvsu.edu", msg="Subject:Surprise!!\n\nI love you")
#     # Close connection
#     connection.close()

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

my_email = "tsounguc@mail.gvsu.edu"
password = ""

date_of_birth = dt.datetime(year=1996, month=7, day=24)

with open("quotes.txt") as file:
    content = file.readlines()
    quote = random.choice(content)
if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday Motivation\n\n{quote}")
