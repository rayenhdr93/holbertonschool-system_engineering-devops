#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv

if __name__ == "__main__":
    '''fixin the module'''
    list = []
    alltodos = 0
    comptodos = 0
    URL1 = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response1 = get(URL1)
    response2 = get(URL2)
    todos = response1.json()
    users = response2.json()
    for i in range(0, len(todos)):
        if (((todos[i]["userId"]) == int(argv[1]))):
            alltodos += 1
            if (todos[i]["completed"]):
                comptodos += 1
                list = list + [(todos[i]["title"])]
    print("Employee {} is done with tasks({}/{}):".format(
        users["name"], comptodos, alltodos))
    for i in range(0, len(list)):
        print("\t", list[i])
