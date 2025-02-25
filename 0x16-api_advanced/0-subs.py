#!/usr/bin/python3
"""
Module to query the Reddit API and return the num of subs
for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the num of subs for a given subreddit
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0