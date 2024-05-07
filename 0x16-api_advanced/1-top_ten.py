#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    function that prints the titles of the first 10 hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    header = {'User-Agent': 'Alx-User_Agent'}
    response = requests.get(url, headers=header).json()

    try:
        for post in response.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
