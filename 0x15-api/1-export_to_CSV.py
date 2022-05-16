#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv

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
    f = open('./{}.csv'.format(argv[1]), 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for i in range(0, len(tod)):
        if (((tod[i]["userId"]) == int(argv[1]))):
            writer.writerow([str(
                tod[i]["userId"]), u, tod[i]["completed"], tod[i]["title"]])
    f.close()
