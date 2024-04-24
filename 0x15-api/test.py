#!/usr/bin/python3
import requests
import sys

def get_employee_info(employee_id):
    # Fetching employee information
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetching TODO list for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Counting completed tasks
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)
    total_tasks = len(todos_data)

    # Displaying employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_info(employee_id)
