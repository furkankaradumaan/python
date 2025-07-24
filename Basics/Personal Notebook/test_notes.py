import unittest
from notes import Note


class TestNote(unittest.TestCase):
    
    def setUp(self):
        self.note1 = Note(1, "Note Title1", "Note Content1")


    def test_fields(self):
        
        self.assertEqual(self.note1.note_id, 1)
        self.assertEqual(self.note1.title, "Note Title1")
        self.assertEqual(self.note1.content, "Note Content1")

    
    
