#!/usr/bin/python3
"""
Python script that uses the JSONPlaceholder API to export data
about all tasks from all employees in JSON format.
"""

import json
import requests


def export_all_tasks():
    # Send GET request to retrieve all users
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Create a dictionary to store tasks for each user
    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        # Send GET request to retrieve tasks for the current user
        tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        tasks = tasks_response.json()

        # Store tasks for the current user in the dictionary
        user_tasks = []
        for task in tasks:
            task_data = {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            }
            user_tasks.append(task_data)

        all_tasks[user_id] = user_tasks

    # Export all tasks to a JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == '__main__':
    export_all_tasks()

