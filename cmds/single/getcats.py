import requests
from os import chdir
from time import sleep

def getcats(count, folder):
    id = 0
    chdir(folder)
    for i in range(count):
        id += 1
        try:
            sleep(1)
            response = requests.get("https://thiscatdoesnotexist.com")
            with open(f'cat{id}.png', 'wb') as file:
                file.write(response.content)
                file.close()
        except:
            print("Error.")
