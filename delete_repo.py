import requests
import os
import json
import threading

def print_message(message):
    print(message)

token = os.environ.get("PAT")
reponame = input("Please enter the repo name you want to delete : ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

username = input("Please enter your GitHub username: ")
r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)
print(r.status_code)  # Use r.status_code to get the HTTP status code

if r.status_code == 204:  # Use r.status_code for comparison
    t = threading.Thread(target=print_message, args=("The repository deleted successfully",))
    t.start()
else:
    t = threading.Thread(target=print_message, args=("Error occurred! Repository not removed",))
    t.start()

