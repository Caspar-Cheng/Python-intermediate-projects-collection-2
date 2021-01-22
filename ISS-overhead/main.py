import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -27.469770
MY_LONG = 153.025131
EMAIL = "jodfoiahf@gmail.com"
PASSWORD = "kjhfajhidhfiudshoi"


def check_iss_nearby():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        return True


# check whether ISS is above in the sky every 60 secs
while True:
    time.sleep(60)
    if check_iss_nearby() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="casparcheng@yahoo.com",
            msg="Subject:Look Up\n\nThe ISS is above you in the sky~!"
        )
        connection.close()


