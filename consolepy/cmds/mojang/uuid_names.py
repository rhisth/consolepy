import requests
import datetime

def uuid_names(uuid):
    response = requests.get("https://api.mojang.com/user/profiles/" + uuid + "/names")
    if response.status_code == 204:
        print("No content.")
    if response.status_code == 200:
        answer = response.json()
        print(f"Name history:\n {answer[0]['name']}: first.")
        answer.pop(0)
        for el in answer:
            print(f" {el['name']}: {datetime.datetime.fromtimestamp(el['changedToAt'] / 1000).strftime('%Y-%m-%d/%H:%M:%S')}.")
