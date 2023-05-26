#!/usr/bin/python3

"""
This script fetches and exports data about an employee's tasks in CSV format
using a provided REST API.
"""

import csv
import requests
import sys

def export_employee_tasks_to_csv(employee_id):
    """
    Fetches the employee's tasks and exports them to a CSV file.
    """

    # Fetch employee data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        # Prepare CSV filename
        filename = f"{employee_id}.csv"

        # Open CSV file in write mode
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write tasks to CSV
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_data['username'],
                    str(task['completed']),
                    task['title']
                ])

        print(f"Tasks exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_tasks_to_csv(employee_id)

