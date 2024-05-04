import requests
import os
import json
import threading

def print_message(message):
    print(message)

data = {"type": "all", "sort":"full_name", "direction": "asc"}
username = input("Please enter your GitHub username: ")
output = requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data))
output = json.loads(output.text)

t=threading.Thread(target=print_message,args=("The list of Repository in ascending order",))
t.start()
for reponame in output:
    print(reponame['name'])

data = {"type": "owner", "direction": "desc"}
username = input("Please enter your GitHub username: ")
output = requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data))
output = json.loads(output.text)

t=threading.Thread(target=print_message,args=("The list of Repository in descending order",))
t.start()
for reponame in output:
    print(reponame['name'])


