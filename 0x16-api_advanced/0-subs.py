#!/usr/bin/python3
'''pycode'''


import requests


def number_of_subscribers(subreddit):
    '''def'''
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "rayen"},)
    x = str(req)
    if x[:16] == '<Response [404]>':
        return 0
    else:
        x = req.json().get("data").get("subscribers")
    return (x)
