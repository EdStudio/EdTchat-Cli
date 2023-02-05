import requests
from getpass import getpass  # Hide password input
import os

# Class
from env import Env


class User:
    def __init__(self, id, name, email, displayName, token, server):
        self.id = id
        self.name = name
        self.email = email
        self.displayName = displayName
        self.token = token
        self.server = server


def passwordLogin(username, password, server):
    url = f"http://{server}/api/v1/auth"
    myobj = {'username': username, 'password': password}

    x = requests.post(url, data=myobj)
    if x.status_code == 200:
        return x.json()
    else:
        return False


def loopAsk(message, type="text"):
    value = ""
    while value == "":
        if(type == "text"):
            value = input(message)
        elif(type == "password"):
            value = getpass(message)
    return value


env = Env()
user = User(0, "", "", "", "", "")

# Login loop
while user.id == 0:
    username = loopAsk("Username: ")
    password = loopAsk("Password: ", "password")
    server = input("Server URL (localhost:3000) : ") or "localhost:3000"

    data = passwordLogin(username, password, server)

    if not data:
        print("Login failed")
    else:
        user.id = -1  # TO DO: Get user id from server
        user.name = username
        user.token = data["token"]

        # Save token to .env file
        env.set("token", str(user.token))
        env.set("server", server)

print("Logged in as " + user.name)
