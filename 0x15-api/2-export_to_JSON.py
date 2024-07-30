#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress, and exports it to JSON.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_response.raise_for_status()
        todos_response.raise_for_status()

        user = user_response.json()
        todos = todos_response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")
        return None, None

    employee_name = user.get('name')
    if not employee_name:
        print("Error: Employee not found.")
        return None, None

    return user, todos


def export_to_json(user, todos):
    user_id = user.get('id')
    username = user.get('username')
    filename = f"{user_id}.json"

    tasks = [
        {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        for task in todos
    ]

    data = {str(user_id): tasks}

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_data, todos_data = get_employee_todo_progress(employee_id)
    if user_data and todos_data:
        export_to_json(user_data, todos_data)
