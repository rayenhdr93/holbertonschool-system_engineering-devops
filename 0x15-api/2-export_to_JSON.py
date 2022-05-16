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
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response1 = get(URL1)
    response2 = get(URL2)
    tod = response1.json()
    users = response2.json()
    u = users["username"]
    for i in range(0, len(tod)):
        if (((tod[i]["userId"]) == int(argv[1]))):
            dict = {}
            dict["task"] = tod[i]["title"]
            dict["completed"] = tod[i]["completed"]
            dict["username"] = u
            list.append(dict)
    dict2 = {}
    dict2[argv[1]] = list
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(dict2, f)
