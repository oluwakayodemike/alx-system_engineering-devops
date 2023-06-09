#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API,
parse the titles of all hot articles,
and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.

        after (str): The 'after' parameter to paginate through
        the API responses (default=None).

        count_dict (dict): The dictionary to store the
        counts of keywords (default={})/

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent header
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word in count_dict:
                        count_dict[word] += count
                    else:
                        count_dict[word] = count

        after = data["data"]["after"]
        if after is not None:
            return count_words{
                    subreddit,
                    word_list,
                    after = after,
                    count_dict = count_dict
            }
        else:
            # Sort by count (descending) and then keyword (ascending)
            sorted_counts = sorted(
                count_dict.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
    else:
        return None
