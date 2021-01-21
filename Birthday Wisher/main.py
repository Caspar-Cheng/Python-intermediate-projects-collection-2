import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "12345467826@gmail.com"
PASSWORD = "this_is_fake_one"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter_content = letter_file.read()
        person = birthday_dict[today]
        new_letter = letter_content.replace("[NAME]", person["name"])

    # use smtp to send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday, {person['name']}\n\n{new_letter}."
        )


