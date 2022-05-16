#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv
import json

if __name__ == "__main__":
    '''fixin the module'''

    URL1 = "https://jsonplaceholder.typicode.com/todos/"
    response1 = get(URL1)
    tod = response1.json()
    dict2 = {}
    for x in range(1, 11):
        URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(str(x))
        response2 = get(URL2)
        users = response2.json()
        u = users["username"]
        list = []
        for i in range(0, len(tod)):
            if (((tod[i]["userId"]) == int(x))):
                dict = {}
                dict["username"] = u
                dict["task"] = tod[i]["title"]
                dict["completed"] = tod[i]["completed"]
                list.append(dict)
        dict2[x] = list
        with open("todo_all_employees.json".format(x), 'a') as f:
            json.dump(dict2, f)
