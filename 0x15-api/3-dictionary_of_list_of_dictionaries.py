#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv
import json

if __name__ == "__main__":
    '''fixin the module'''

    URL1 = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/"
    response1 = get(URL1)
    response2 = get(URL2)
    tod = response1.json()
    users = response2.json()
    dict2 = {}
    for x in range(1, len(users) + 1):
        list = []
        for i in range(0, len(tod)):
            if ((tod[i]["userId"]) == x):
                dict = {}
                dict["username"] = users[x - 1]["username"]
                dict["task"] = tod[i]["title"]
                dict["completed"] = tod[i]["completed"]
                list.append(dict)
        dict2[x] = list
    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict2, f)
