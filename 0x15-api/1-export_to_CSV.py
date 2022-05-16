#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv

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
    u = users["username"]
    f = open('./{}.csv'.format(argv[1]), 'w')
    writer = csv.writer(f)
    for i in range(0, len(todos)):
        if (((todos[i]["userId"]) == int(argv[1]))):
            writer.writerow([str(
                todos[i]["userId"]), u, todos[i]["completed"], todos[i]["title"]])
    f.close()
