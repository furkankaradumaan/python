from notes import Note

def get_id():
    
    note_id = None

    while True:
        try:
            note_id = int(input("ID number: "))
        except ValueError as e:
            print(e)
        else:
            return note_id

def get_content():
    content = ""

    while True:
        try:
            line = input()
        except EOFError:
            break

        content += f"{line}\n"

    return content
            

def create_note():

    note_id: int = None
    title: str = None
    content: str = None
    
    note_id = get_id()
    title = input("Title: ")
    content = get_content()
    
    return Note(note_id, title, content)
