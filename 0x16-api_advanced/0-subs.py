#!/usr/bin/python3
"""Return the total number of subscribers on a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns
    the number of subscribers (not active users, total
    subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.

    Hint: No authentication is necessary for most features
    of the Reddit API. If you’re getting errors related
    to Too Many Requests, ensure you’re setting a custom User-Agent.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Alx-User-Agent"}
    sub_response = requests.get(url, headers=header, allow_redirects=False)

    if sub_response.status_code == 200:
        data = sub_response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    return 0
