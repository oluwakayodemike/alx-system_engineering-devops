
rt sys
import requests

def gather_data_from_API(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.

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
    employee_name = employee['name']

    # Make a GET request for the employee's TODO list
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Display the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_API(employee_id)

