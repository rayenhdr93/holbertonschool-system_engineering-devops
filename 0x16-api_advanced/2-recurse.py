#!/usr/bin/python3
'''pycode'''


import requests


def recurse(subreddit, hot_list=[]):
    '''def'''
    req = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
        headers={'User-agent': 'rayen'})
    x = str(req)
    if x[11] != '2':
        return(None)
    else:
        for i in range(0, (len(req.json().get("data").get("children")))):
            element = req.json().get("data").get("children")[i].get(
                "data").get("title")
            i = i + 1
            hot_list.append(element)
        return(hot_list)
