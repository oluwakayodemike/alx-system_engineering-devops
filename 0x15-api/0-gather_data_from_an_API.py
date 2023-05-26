import sys
import requests

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Make a GET request to the API
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos = response.json()

# Filter completed tasks
completed_tasks = [todo for todo in todos if todo['completed']]

# Get the employee name
employee_name = todos[0]['name']

# Display the progress
print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")
for task in completed_tasks:
    print("\t", task['title'])

