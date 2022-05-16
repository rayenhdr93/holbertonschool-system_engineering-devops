#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv
import json

if __name__ == "__main__":
    '''fixin the module'''
    list = []
    URL1 = "https://jsonplaceholder.typicode.com/todos/"
    response1 = get(URL1)
    tod = response1.json()
    for x in range(1, 10):
        URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(str(x))
        response2 = get(URL2)
        users = response2.json()
        u = users["username"]
        for i in range(0, len(tod)):
            if (((tod[i]["userId"]) == int(x))):
                dict = {}
                dict["task"] = tod[i]["title"]
                dict["completed"] = tod[i]["completed"]
                dict["username"] = u
                list.append(dict)
        dict2 = {}
        dict2[x] = list
        with open("todo_all_employees.json".format(x), 'a') as f:
            json.dump(dict2, f)
