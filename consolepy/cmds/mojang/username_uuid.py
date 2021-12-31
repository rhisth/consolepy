import requests

def username_uuid(username):
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if response.status_code == 204:
        print("No content.")
    if response.status_code == 200:
        answer = response.json()
        print("Username: " + answer["name"])
        print("UUID: " + answer["id"])
