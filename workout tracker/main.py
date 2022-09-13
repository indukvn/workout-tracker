import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


# add_id and api_key from Nutritionix API website
APP_ID = "your app id"
API_KEY = "your api key"

GENDER = "gender"
WEIGHT_KG = "your weight"
HEIGHT_CM = "your height"
AGE = "your age"

query_input = input("Tell which exercise you did: ")

exercise_end_pt = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": query_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_end_pt, data=exercise_params, headers=headers)
res = response.json()

today = datetime.now()
present_date = today.strftime("%d/%m/%Y")
present_time = today.strftime("%H:%M:%S")

# sheety_end_pt from sheety
# create a new project and upload existing or new sheet to get the end point
sheety_end_pt = "your end point"


for exercise in res["exercises"]:
    sheety_params = {
        "workout": {
            "date": present_date,
            "time": present_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
}

    # for basic authentication
    sheet_response = requests.post(sheety_end_pt, json=sheety_params, auth=('your username in sheety authentication'
                                                                            , 'your password in sheety authentication'))
    print(sheet_response.text)

    # to post the data into sheets without authentication
    # response = requests.post(sheety_end_pt, json=sheety_params)
    # print(response.text)
