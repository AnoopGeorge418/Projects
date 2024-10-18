import csv

def save_task(name, description):
    with open('tasks.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, description])
    print('Task saved to CSV file.')

def add():
    try:
        number_of_tasks = int(input('Enter the number of tasks you want to add: '))
        count = 0
        while count < number_of_tasks:
            name_of_task = input('Task name: ').title()
            description = input(f'Description for {name_of_task}: ').capitalize()
            save_task(name_of_task, description)
            count += 1
        print('All tasks added successfully.')
    except ValueError:
        print('Please enter a number.')

def view():
    print('\nTasks:')
    try:
        with open('tasks.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for idx, row in enumerate(reader, start=1):
                print(f'{idx} - {row[0]}: {row[1]}')
    except FileNotFoundError:
        print('No tasks found. Please add tasks first.')

def update():
    view()
    tasks = []
    with open('tasks.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader]
    
    while True:
        task_name = input('Enter the name of the task you want to update (or type "done" to go back): ').title()
        if task_name.lower() == 'done':
            break
        
        for task in tasks:
            if task[0] == task_name:
                new_description = input(f'Enter the new description for {task_name}: ').capitalize()
                task[1] = new_description
                print(f'Task "{task_name}" updated successfully.')
                break
        else:
            print(f'Task "{task_name}" not found.')
    
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def delete():
    view()
    tasks = []
    with open('tasks.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader]
    
    while True:
        task_name = input('Enter the name of the task you want to delete (or type "done" to go back): ').title()
        if task_name.lower() == 'done':
            break

        for idx, task in enumerate(tasks):
            if task[0] == task_name:
                del tasks[idx]
                print(f'Task "{task_name}" deleted successfully.')
                break
        else:
            print(f'Task "{task_name}" not found.')
    
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
