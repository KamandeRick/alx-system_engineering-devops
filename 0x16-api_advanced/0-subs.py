#!/usr/bin/python3
"""
Module Docs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function Docs
    """
    # Set up the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        #'User-Agent': 'CustomScript/1.0 (by /u/YourRedditUsername)'
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is not found or any other error occurs, return 0
            return 0
    except requests.RequestException:
        # If there's any exception during the request, return 0
        return 0
