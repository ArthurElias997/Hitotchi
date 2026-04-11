import unittest
from unittest.mock import patch
from src.utils import get_user_choice

class TestUtils(unittest.TestCase):
    @patch('builtins.input', side_effect=['x', '1'])
    def test_choice(self, mock_input):
        self.assertEqual(get_user_choice("Escolha:", ['1', '2']), '1')