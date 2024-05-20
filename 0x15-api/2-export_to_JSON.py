#!/usr/bin/python3
""" Exports tasks owned by a user to a JSON file. """
import json
import requests
import sys


def export_to_json(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(user_id): tasks}

    json_filename = f"{user_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <user_id>")
        sys.exit(1)
    user_id = sys.argv[1]
    try:
        int(user_id)
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)
    export_to_json(user_id)
