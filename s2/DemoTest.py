import unittest

class DemoTest(unittest.TestCase):
    def test_number(self):
        self.assertEqual(1, 1, "Uno no es igual a dos")

