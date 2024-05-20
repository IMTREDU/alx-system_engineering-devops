#!/usr/bin/python3
""" Export data in the JSON format. """

import json
import requests


def fetch_user_data():
    """Retrieve user information and to-do lists for all employees."""
    base_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base_url + "users").json()

    export_data = {}
    for user in users:
        user_id = user["id"]
        todos_url = base_url + f"todos?userId={user_id}"
        todos = requests.get(todos_url).json()

        export_data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todos
        ]

    return export_data


if __name__ == "__main__":
    export_data = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(export_data, jsonfile, indent=4)
