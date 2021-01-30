import requests
from datetime import datetime


# create a workout tracking sheet
NUTRITIONIX_ID = "......."
NUTRITIONIX_API = "..................."

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/.../.../sheet1"
sheet_api = "........"

exercise_text = input("Which exercise you did: ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API
}
parameters = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": "...",
    "height_cm": "...",
    "age": "..."
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


# use Sheety to connect this project with my google sheet by linking google sheet url to Sheety project
today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheet_headers = {
        "Authorization": f"Bearer {sheet_api}",
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_headers)


