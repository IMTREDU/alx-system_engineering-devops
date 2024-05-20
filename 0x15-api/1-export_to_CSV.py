#!/usr/bin/python3
""" Exports tasks owned by a user to a CSV file. """
import csv
import requests
import sys


def export_to_csv(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([
                user_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <user_id>")
        sys.exit(1)
    user_id = sys.argv[1]
    try:
        int(user_id)
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)
    export_to_csv(user_id)
