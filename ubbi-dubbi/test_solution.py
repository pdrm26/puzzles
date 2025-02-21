import unittest
from solution import ubbi_dubbi


class TestUbbiDubbi(unittest.TestCase):
    def test_words(self):
        self.assertEqual(ubbi_dubbi("elephant"), "ubelubephubant")
        self.assertEqual(ubbi_dubbi("octopus"), "uboctubopubus")
        self.assertEqual(ubbi_dubbi("program"), "prubogrubam")
        self.assertEqual(ubbi_dubbi("milk"), "mubilk")
        self.assertEqual(ubbi_dubbi("soap"), "suboubap")


if __name__ == "__main__":
    unittest.main()
