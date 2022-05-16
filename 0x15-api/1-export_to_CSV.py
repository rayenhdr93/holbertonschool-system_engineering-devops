#!/usr/bin/python3
'''Gather data from an API'''


from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    '''fixin the module'''
    list = []
    alltod = 0
    comptod = 0
    URL1 = "https://jsonplaceholder.typicode.com/tod/"
    URL2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response1 = get(URL1)
    response2 = get(URL2)
    tod = response1.json()
    users = response2.json()
    u = users["username"]
    f = open('./{}.csv'.format(argv[1]), 'w')
    writer = csv.writer(f)
    for i in range(0, len(tod)):
        if (((tod[i]["userId"]) == int(argv[1]))):
            writer.writerow([str(
                tod[i]["userId"]), u, tod[i]["completed"], tod[i]["title"]])
    f.close()
