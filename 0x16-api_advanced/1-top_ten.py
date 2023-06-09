#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Set a custom User-Agent header
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
