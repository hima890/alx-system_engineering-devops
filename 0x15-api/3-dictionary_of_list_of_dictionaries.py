#!/usr/bin/python3
""""Python script to export data in the JSON format"""

import json
import requests


def fetch_data():
    # Fetch data from the API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


def fetch_users():
    # Fetch user data from the API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def create_task_record(users, todos):
    # Create a dictionary of users with their tasks
    user_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks[user_id] = []

        for todo in todos:
            if todo['userId'] == user['id']:
                task_record = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks[user_id].append(task_record)

    return user_tasks


def save_to_json(data, filename):
    # Save the data to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    todos = fetch_data()
    users = fetch_users()
    task_data = create_task_record(users, todos)
    save_to_json(task_data, 'todo_all_employees.json')


if __name__ == "__main__":
    main()
