#!/usr/bin/python3
'''pycode'''


import requests


def top_ten(subreddit):
    '''def'''
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit),
        headers={'User-agent': 'rayen'})
    x = str(req)
    if x[11] != '2':
        print("None")
    else:
        for i in range(0, 10):
            print(req.json().get("data").get("children")[i].get(
                "data").get("title"))
