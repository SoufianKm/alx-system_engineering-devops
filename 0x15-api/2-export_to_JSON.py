#!/usr/bin/python3
""" script to export data in the json format """
import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        json.dump({sys.argv[1]: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("name")
                } for todo in todos]}, jsonfile)
