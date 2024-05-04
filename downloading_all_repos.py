import requests
import os
import threading

# Replace with your GitHub username and personal access token
username = "dawoodkhatri1"
access_token = os.environ.get("PAT")

# Set the base URL for the GitHub API
base_url = "https://api.github.com"

# Create a session with the access token to authenticate requests
session = requests.Session()
session.auth = (username, access_token)

# Function to clone a repository
def clone_repository(repository):
    name = repository["name"]
    clone_url = repository["clone_url"]
    print(f"Cloning {name} from {clone_url}")
    os.system(f"git clone {clone_url}")

# Get the list of repositories for the authenticated user
repositories_url = f"{base_url}/user/repos"
response = session.get(repositories_url)
repositories = response.json()

# Create a list to hold thread objects
threads = []

# Loop over the repositories and create a thread for each repository
for repository in repositories:
    # Create a thread for each repository and pass the clone_repository function as the target
    thread = threading.Thread(target=clone_repository, args=(repository,))
    # Start the thread
    thread.start()
    # Add the thread to the list
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
