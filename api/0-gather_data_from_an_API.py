#!/usr/bin/python3
""" Gather data from an API
    API used: https://jsonplaceholder.typicode.com/"""
from sys import argv
import requests


if __name__ == '__main__':
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()

    real_name = ""
    for each_element in user:
        if each_element.get('id') == int(argv[1]):
            real_name = each_element.get('name')
            break

    full_list = []
    for dict in todo:
        if dict.get('userId') == int(argv[1]):
            full_list.append(dict)

    true_elements = []
    for completed in full_list:
        if completed.get('completed'):
            true_elements.append(completed)

    print('Employee {} is done with tasks({}/{}):'.
          format(real_name, len(true_elements), len(full_list)))
    for task in true_elements:
        print('\t {}'.format(task.get('title')))
