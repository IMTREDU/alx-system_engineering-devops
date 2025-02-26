#!/usr/bin/python3
"""
Module to query the Reddit API & return the num of subs
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API & Ret the total num of subs of given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0