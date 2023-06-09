#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API and
return a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles 
        (default=[]).

    Returns:
        list: The list containing the titles of all hot articles.
        Returns None if no results are found or if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent header
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None

