import unittest

from machine import PrizeMachine

class TestPrizeMachine(unittest.TestCase):

    def test_get_input(self):
        test_object = PrizeMachine("basketball")

        test_object.get_input()

        sample_list = ["Abhi", "Kevin", "Sean", "Daryl", "Sean"]

        self.assertEqual(test_object.name_list, sample_list)