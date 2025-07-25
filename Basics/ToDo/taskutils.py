from datetime import date
from todo import Task

def new_task():

    tid: int = None
    task: str = None
    deadline: date = None
    completed: bool = False

    try:
        tid = int(input("ID number: "))
        task = input("Task: ")
        deadline = date.fromisoformat(input("Deadline(yyyy-mm-dd): "))
    except ValueError as e:
        print(e)
    else:
        return Task(tid, task, deadline, completed)

    return None

def remove_task():
    tid: int = None

    try:
        tid = int(input("ID number: "))
        c = Task.remove_task(tid)
    except ValueError as e:
        print(e)
    else:
        return c


def update_task():
    
    tid: int = None
    new_content: str = None
    deadlines: str = None
    new_deadline: date = None
    try:

        tid = int(input("ID number: "))
        new_content = input("New task: ")
        new_deadline = input("New deadline(yyyy-mm-dd): ")

        if deadlines:
            new_deadline = date.strftime(deadlines)        

    except ValueError as e:
        print(e)
    else:
        if Task.task_exists(tid):
            return Task.update_task(tid, new_content, new_deadline)
    
    return 0

def update_completed(completed: bool):

    try:
        tid = int(input("ID number: "))
    except ValueError as e:
        print(e)
    else:
        task = Task.get_task(tid)
        if task:
            task.completed = completed
            return 1
    return 0
        

