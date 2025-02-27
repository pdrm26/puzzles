import unittest
from solution import mysum


class TestMySum(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(mysum(), ())

    def test_numbers(self):
        self.assertEqual(mysum(1, 2, 3), 6)

    def test_strings(self):
        self.assertEqual(mysum("a", "b", "c"), "abc")

    def test_lists(self):
        self.assertEqual(mysum(["a", "b"], ["c"], ["d"]), ["a", "b", "c", "d"])

    def test_tuples(self):
        self.assertEqual(mysum(("a", "b", "c"), (1, 2, 3)), ("a", "b", "c", 1, 2, 3))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            mysum("a", 1)


if __name__ == "__main__":
    unittest.main()
