import requests
import threading
import os
import json

def print_message(message):
    print(message)

token = os.environ.get("PAT")
reponame = input("Please enter the repo name you want to create : ")
GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}
r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r.status_code)  # Use r.status_code to get the HTTP status code

if r.status_code == 201:  # Use r.status_code for comparison
    t = threading.Thread(target=print_message, args=("The repository created successfully",))
    t.start()
else:
    t = threading.Thread(target=print_message, args=("Error occurred! Repository not created",))
    t.start()
