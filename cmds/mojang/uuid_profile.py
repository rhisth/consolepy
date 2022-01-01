import requests
import base64
import json

def uuid_profile(uuid):
    response = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
    if response.status_code == 204:
        print("No content.")
    if response.status_code == 200:
        answer = response.json()['properties'][0]['value']
        answer = base64.b64decode(answer.encode("ascii")).decode('ascii')
        answer = json.loads(answer)
        print(f"Username: {answer['profileName']}\nUUID: {answer['profileId']}\nSkin:\n Url: ", end = "")
        if not "SKIN" in answer["textures"]:
            print("None")
        else:
            print(answer['textures']['SKIN']['url'])
            if not "metadata" in answer["textures"]["SKIN"]:
                print(" Model: default")
            else:
                print(f" Model: slim")
