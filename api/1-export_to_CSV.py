#!/usr/bin/python3
"""Script that uses REST API"""
import requests
from sys import argv
import csv


def to_csv():
    """return API data"""
    user = requests.get("http://jsonplaceholder.typicode.com/users").json()
    for elements in user:
        if elements.get('id') == int(argv[1]):
            USERNAME = elements.get('username')
            break

    task_title = []
    todo = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    for dict in todo:
        if dict.get('userId') == int(argv[1]):
            task_title.append((dict.get('completed'), dict.get('title')))

    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in task_title:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})

if __name__ == "__main__":
    to_csv()