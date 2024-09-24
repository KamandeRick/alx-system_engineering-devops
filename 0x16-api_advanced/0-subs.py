#!/usr/bin/python3
"""
Module to query reddit for nsub count in a sub reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function to query reddit
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get('{}/r/{}/about/.json'.format(url, subreddit),
                            headers=header,
                            allow_redirects=False
                            )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0