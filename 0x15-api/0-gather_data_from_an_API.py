#!/usr/bin/python3
"""Returns to-do list progress information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(link + "todo", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(c)) for c in completed]
