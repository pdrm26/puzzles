import unittest
from solution import firstlast


class TestFirstLast(unittest.TestCase):
    def test_string_input(self):
        self.assertEqual(firstlast("abc"), "ac")
        self.assertEqual(firstlast("a"), "a")
        self.assertEqual(firstlast(""), "")

    def test_list_input(self):
        self.assertEqual(firstlast([1, 2, 3, 4]), [1, 4])
        self.assertEqual(firstlast([1]), [1])
        self.assertEqual(firstlast([]), [])

    def test_tuple_input(self):
        self.assertEqual(firstlast((10, 20, 30)), (10, 30))
        self.assertEqual(firstlast((3,)), (3,))
        self.assertEqual(firstlast(()), ())


if __name__ == "__main__":
    unittest.main()
