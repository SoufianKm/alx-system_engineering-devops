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
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    client_auth = requests.auth.HTTPBasicAuth(
            'LY9-f45QIEy_wbuZRPuRDw', 'bOc_nJ0uRZM0qzeqx_9z7nKN40Ewnw')
    headers = {"User-Agent": "User-Client/0.1 by soufianKm"}
    response = requests.get(
            url, headers=headers,
            auth=client_auth,
            allow_redirects=False)

    if response.status_code == 200 and not response.is_redirect:
        try:
            for post in response.json().get('data').get('children'):
                print(post.get('data').get('title'))
        except Exception:
            print("None")
    else:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])
