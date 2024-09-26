#!/usr/bin/python3
"""Module to querry reddit for subreddit sub count """

import requests


def number_of_subscribers(subreddit):
    """function to query a subreddit and return its sub count"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
