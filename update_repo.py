import requests
import os
import json
import threading

def print_message(message):
    print(message)

token = os.environ.get("PAT")
reponame = input("Please enter the repo name you want to rename : ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

username = input("Please enter your GitHub username: ")
r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)

reponame = input("Please enter the new repo : ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r.status_code)

if r.status_code == 201:  # Use r.status_code for comparison
    t = threading.Thread(target=print_message, args=("The repository Updated successfully",))
    t.start()
else:
    t = threading.Thread(target=print_message, args=("Error occurred! Repository not Updated",))
    t.start()
