#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    client_auth = requests.auth.HTTPBasicAuth(
            'LY9-f45QIEy_wbuZRPuRDw', 'bOc_nJ0uRZM0qzeqx_9z7nKN40Ewnw')
    headers = {"User-Agent": "User-Client/0.1 by soufianKm"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(
            url, headers=headers,
            auth=client_auth,
            params=params,
            allow_redirects=False)

    if response.status_code >= 300 or response.is_redirect:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
