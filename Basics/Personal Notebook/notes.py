import json

class Note:
    
    __all_notes = []
    __json_name = "notes.json"

    def __init__(self, note_id: int, title: str, content: str):

        self.__note_id = note_id
        self.__title = title
        self.__content = content

        Note.__all_notes.append(self)

    def __str__(self):
        return f"Note ID: {self.note_id}\nTitle: {self.title}\nContent: {self.content}"
    @property
    def note_id(self):
        return self.__note_id

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @title.setter
    def title(self, new_title):
        self.__title = new_title
    
    @content.setter
    def content(self, new_content):
        self.__content = new_content
        
    @classmethod
    def to_dictionary(cls):

        d = dict()
        d["notes"] = list()

        for note in cls.__all_notes:
            d_note = dict()
            d_note["id"] = note.note_id 
            d_note["title"] = note.title
            d_note["content"] = note.content

            d["notes"].append(d_note)
        
        return d

    @classmethod
    def initialize_from_json(cls):
        
        with open(cls.__json_name) as jsonfile:
            
            d = json.load(jsonfile)

            for d_note in d["notes"]:
                Note(d_note["id"], d_note["title"], d_note["content"])

    @classmethod
    def save_to_json(cls):

        with open(cls.__json_name, "w") as jsonfile:             
            d = cls.to_dictionary()
            json.dump(d, jsonfile, indent = 4)

    @classmethod
    def list_notes(cls):

        for note in cls.__all_notes:
            print(note)
            print("*" * 100)

    @classmethod
    def remove_note(cls, note_id: int):
        filtered = filter(lambda note: note.note_id == note_id, cls.__all_notes)

        for note in filtered:
            cls.__all_notes.remove(note)
