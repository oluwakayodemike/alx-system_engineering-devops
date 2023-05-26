#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])

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

        # Display progress information
        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        completed_count = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_count, total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

