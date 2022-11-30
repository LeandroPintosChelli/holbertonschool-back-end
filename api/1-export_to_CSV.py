#!/usr/bin/python3
"""Script that uses REST API"""
import requests
from sys import argv
import csv


def to_csv():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    for u in users:
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break

    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    for t in todos:
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})

if __name__ == "__main__":
    to_csv()