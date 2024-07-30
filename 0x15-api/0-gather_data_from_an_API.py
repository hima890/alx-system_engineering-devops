#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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
        return

    employee_name = user.get('name')
    if not employee_name:
        print("Error: Employee not found.")
        return

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]

    response = "Employee {} is done with tasks({}/{}):"
    print(response.format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
