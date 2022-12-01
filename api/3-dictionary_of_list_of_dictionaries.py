#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""
import json
import requests


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump({
            u.get("id"): [{
                "task": dict.get("title"),
                "completed": dict.get("completed"),
                "username": dict.get("username")
            } for dict in requests.get(url + "todos",
                                       params={"userId": u.get("id")}).json()]
            for u in users}, JSONfile)
