import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()  # load the .env file

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
PIXEL_HEADER = {
    "X-USER-TOKEN": TOKEN
}

# TODO: Create a new user (POST)
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)

# TODO: Create a graph definition (POST)
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Min",
    "type": "int",
    "color": "kuro",
    "timezone": "Asia/Taipei",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(response.text)


not_over = True
while not_over:

    answer = input(
        "What would you like to do? (NEW, UPDATE, DELETE or EXIT)").lower()

    if answer == "new":

        # TODO: Get a graph (POST)
        pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

        today = datetime.now()

        pixel_config = {
            # strftime can format the time as you want
            "date":  today.strftime("%Y%m%d"),
            "quantity": input("How many minutes do you code today? "),
        }
        response = requests.post(url=pixel_creation_endpoint,
                                 json=pixel_config, headers=PIXEL_HEADER)
        print(response.text)
    elif answer == "update":

        # TODO: Update a graph (PUT)
        date = input("Which date would you like to revise? (YYYYMMDD)")
        pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
        pixel_update_config = {
            "date":  f"{date}",
            "quantity": input("How many minutes do you code today? "),
        }

        response = requests.put(url=pixel_update_endpoint,
                                json=pixel_update_config, headers=PIXEL_HEADER)
        print(response.text)
    elif answer == "delete":

        # TODO: Delete a graph (DELETE)
        date = input("Which day would you like to delete? (YYYYMMDD)")
        pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
        response = requests.delete(
            url=pixel_delete_endpoint, headers=PIXEL_HEADER)
        print(response.text)

    elif answer == "exit":
        print("See you next time :D")
        not_over = False
