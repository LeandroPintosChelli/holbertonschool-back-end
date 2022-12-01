#!/usr/bin/python3
"""
Export to JSON
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url).json()

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(url).json()

    dict = [{"task": dict.get("title"),
             "username": user.get('username'),
             "completed": dict.get("completed")} for dict in todo]

    new_dict = {}
    new_dict[uid] = dict
    with open("{}.json".format(uid), 'w') as JSONfile:
        json.dump(new_dict, JSONfile)
