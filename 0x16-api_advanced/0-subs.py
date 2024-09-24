#!/usr/bin/python3
"""Querying reddit for number of subs in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive sub count"""

    # Redit endpoint for gathering subreddit info
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom agent
    headers = {'User-Agent': 'My user Agent 1.0'}

    # get Request sent to api
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Redirect if request not successful
    if response.status_code == 200:
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
