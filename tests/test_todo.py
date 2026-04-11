import unittest
from src.todo import add_todo, list_todos, mark_done, remove_todo, clear_todos, todos

class TestTodo(unittest.TestCase):
    def setUp(self): clear_todos()

    def test_add_todo(self):
        add_todo("Estudar")
        self.assertEqual(len(todos), 1)

    def test_add_empty(self):
        with self.assertRaises(ValueError): add_todo("")

    def test_mark_done(self):
        add_todo("Ler")
        mark_done(0)
        self.assertTrue(todos[0]["done"])