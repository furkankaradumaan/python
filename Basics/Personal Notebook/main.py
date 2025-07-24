import sys
from notes import *
from noteutils import *

def main(argv: tuple):
    
    if len(argv) == 1:
        print("Usage: <command>")

    Note.initialize_from_json()

    command = argv[1] 

    match command:
        case "add":
            create_note()
        case "list":
            Note.list_notes()
        case "remove":
            note_id = get_id()
            Note.remove_note(note_id)
        case _:
            print(f"Unknown command {command}")

    Note.save_to_json()

if __name__ == "__main__":
    main(sys.argv)
