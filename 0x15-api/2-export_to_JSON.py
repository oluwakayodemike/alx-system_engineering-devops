import sys
import requests
import json

def export_to_JSON(employee_id):
    """
    Retrieves and exports the employee's TODO list in JSON format.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    # Make a GET request to the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    # Get employee details
    username = employee['username']

    # Make a GET request for the employee's TODO list
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Create the JSON data
    data = {str(employee_id): []}
    for todo in todos:
        task_title = todo['title']
        completed = todo['completed']
        data[str(employee_id)].append({"task": task_title, "completed": completed, "username": username})

    # Export data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_JSON(employee_id)

