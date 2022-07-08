#!/usr/bin/python3
'''pycode'''


import requests
def number_of_subscribers(subreddit):
    '''def'''
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},)
    x = str(sub_info)
    if x[:16] == '<Response [404]>':
        return 0
    else:
        x = sub_info.json().get("data").get("subscribers")
    return (x)
