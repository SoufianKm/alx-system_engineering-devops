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
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    client_auth = requests.auth.HTTPBasicAuth(
            'LY9-f45QIEy_wbuZRPuRDw', 'bOc_nJ0uRZM0qzeqx_9z7nKN40Ewnw')
    headers = {"User-Agent": "User-Client/0.1 by soufianKm"}
    response = requests.get(
            url, headers=headers,
            auth=client_auth,
            allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
