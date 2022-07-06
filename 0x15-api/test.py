#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
if __name__ == "__main__":
    '''fixin the module'''
    URL1 = "https://jsonplaceholder.typicode.com/todos/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(argv[1])
    response1 = get(URL1)
    response2 = get(URL2)
    todos = response1.json()
    users = response2.json()
    print(users)
    

