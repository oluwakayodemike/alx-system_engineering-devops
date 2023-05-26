#!/usr/bin/python3

"""
This script fetches and exports information about an employee's TODO list progress
in CSV format using a provided REST API.
"""

import csv
import requests
import sys


def export_employee_todo_progress_to_csv(employee_id):
    """
    Fetches the employee's TODO list progress and exports it in CSV format.
    """

    # Fetch employee data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todos_data if task['completed']]

        # Prepare CSV file name
        csv_file_name = f"{employee_id}.csv"

        # Prepare CSV data
        csv_data = []
        for task in completed_tasks:
            task_id = task['id']
            task_title = task['title']
            task_completed_status = str(task['completed'])
            csv_data.append([employee_id, employee_data['username'], task_completed_status, task_title])

        # Write CSV file
        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
            writer.writerows(csv_data)

        print(f"Data exported to {csv_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_progress_to_csv(employee_id)

