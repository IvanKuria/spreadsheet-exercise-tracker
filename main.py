import requests
from datetime import datetime as dt
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv(f"{os.getcwd()}/Users/ivankuria/PycharmProjects/exercise-tracker/.env")

'''

LLM API Information

'''
# APP_ID and API_KEY have been stored as environment variables
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

exercise_recommendation_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
QUERY = input("Tell me which exercises you did?")

# stores the necessary parameters
exercise_recommendation_params = {
    "query": QUERY
}

# stores the header information
exercise_recommendation_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_response = requests.post(url=exercise_recommendation_endpoint, json=exercise_recommendation_params,
                                  headers=exercise_recommendation_headers)


'''

Sheety API Information

'''

# PASSWORD, USERNAME AND sheety_endpoint have been stored as environment variables


PASSWORD = os.environ.get("PASSWORD")
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
sheety_endpoint = os.environ.get("sheety_endpoint")

today = dt.now().strftime("%d/%m/%Y")
time = dt.now().strftime("%X")


exercises = exercise_response.json()

# iterates through each exercise and populates the data
for exercise in exercises["exercises"]:
    sheety_param = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    sheety_headers = {
        "Authorization": f"Basic {TOKEN}",
        "username": USERNAME,
        "password": PASSWORD
    }
    sheety_response = requests.post(url="sheety_endpoint", json=sheety_param, headers=sheety_headers)
    print(sheety_response.text)
