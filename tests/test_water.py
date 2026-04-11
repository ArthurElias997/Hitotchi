import unittest
from src.water import set_goal, add_water, get_progress, reset_water

class TestWater(unittest.TestCase):
    def setUp(self): reset_water()

    def test_add_water(self):
        add_water(200)
        curr, _ = get_progress()
        self.assertEqual(curr, 200)

    def test_negative_water(self):
        with self.assertRaises(ValueError):
            add_water(-50)