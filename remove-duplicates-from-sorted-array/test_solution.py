import unittest
from solution import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        nums = []
        expected_k = 0

        k = self.solution.removeDuplicates(nums)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [5]
        expected_k = 1

        k = self.solution.removeDuplicates(nums)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, [5])

    def test_all_duplicates(self):
        nums = [1, 1, 1, 1, 1, 1]
        expected_k = 1

        k = self.solution.removeDuplicates(nums)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, [1])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        expected_k = 5

        k = self.solution.removeDuplicates(nums)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
