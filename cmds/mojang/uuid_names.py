import requests
import datetime

def uuid_names(uuid):
    response = requests.get("https://api.mojang.com/user/profiles/" + uuid + "/names")
    if response.status_code == 204:
        print("No content.")
    if response.status_code == 200:
        answer = response.json()
        print("Name history:")
        print(f" {answer[0]['name']}: first.")
        answer.pop(0)
        for element in answer:
            print(f" {element['name']}: {datetime.datetime.fromtimestamp(element['changedToAt'] / 1000).strftime('%Y-%m-%d/%H:%M:%S')}.")
