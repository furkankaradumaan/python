import sys
from todo import Task
from taskutils import *

def main(argv):
    
    if len(argv) < 1:
        print("Usage: python3 main <command>")
        exit(1)

    command = argv[1]
    

    Task.load_from_json()
    match command:
        case "new":
            new_task()
        case "list":
            Task.list_tasks()
        case "remove":
            print(remove_task())
        case "update":
            print(update_task())
        case "complete":
            print(update_completed(True))
        case "uncomplete":
            print(update_completed(False))
        case _:
            print(f"Invalid command {command}")
        
    Task.save_to_json()

if __name__ == "__main__":
    main(sys.argv)
