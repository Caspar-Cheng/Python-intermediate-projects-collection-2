# https://pixe.la/


import requests
import datetime

TOKEN = "Your_own_token"
USERNAME = "your_name"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# Create username of pixela API

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)


# create a new graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Times",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)

today = datetime.date.today()
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_param = {
    "date": today.strftime("%Y%m%d"), # set particular format via .strftime() function
    "quantity": "1"
}

response = requests.post(url=post_endpoint, json=pixel_param, headers=headers)


# to delete a pixel:
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_param['date']}"
# response = requests.delete(url=delete_endpoint, headers=headers)





