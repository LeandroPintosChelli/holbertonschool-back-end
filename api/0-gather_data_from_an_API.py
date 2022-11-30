#!/usr/bin/python3
"""Gather data from an API"""
import urllib
import requests
import json


data = requests.get('https://jsonplaceholder.typicode.com/todos/1').text

print(data)
