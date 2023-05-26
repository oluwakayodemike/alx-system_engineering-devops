#!/usr/bin/python3

"""
This script fetches and displays information about an employee's TODO list progress
using a provided REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetches the employee's TODO list progress and returns it as a formatted string.
    """

    # Fetch employee data
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todos_data if task['completed']]

        # Prepare progress information
        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        completed_count = len(completed_tasks)

        # Format progress information
        progress_info = "Employee {} is done with tasks({}/{}):\n".format(
            employee_name, completed_count, total_tasks
        )
        task_titles = "\n".join("\t{}".format(task['title']) for task in completed_tasks)

        return progress_info + task_titles

    except requests.exceptions.RequestException as e:
        return "An error occurred: {}".format(e)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_progress = get_employee_todo_progress(employee_id)
    print(todo_progress)

