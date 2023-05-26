#!/usr/bin/python3
"""
Exports employee's TODO list progress to CSV format.
"""

import sys
import requests
import csv

def export_to_csv(employee_id):
    """
    Exports employee's TODO list progress to CSV format.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    # Make a GET request to the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Get employee details
    employee_name = todos[0]['name']
    employee_username = todos[0]['username']

    # Prepare data for CSV export
    data = []
    for task in todos:
        task_id = task['id']
        task_title = task['title']
        task_completed = task['completed']
        data.append([task_id, employee_username, str(task_completed), task_title])

    # Export data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Data exported to", filename)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)

