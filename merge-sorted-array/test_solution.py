from solution import Solution
import pytest


test_cases = [
    {
        "name": "Example 1",
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6],
    },
    {"name": "Example 2", "nums1": [1], "m": 1, "nums2": [], "n": 0, "expected": [1]},
    {"name": "Example 3", "nums1": [0], "m": 0, "nums2": [1], "n": 1, "expected": [1]},
    {
        "name": "Both empty arrays",
        "nums1": [],
        "m": 0,
        "nums2": [],
        "n": 0,
        "expected": [],
    },
    {
        "name": "nums2 elements all smaller",
        "nums1": [4, 5, 6, 0, 0, 0],
        "m": 3,
        "nums2": [1, 2, 3],
        "n": 3,
        "expected": [1, 2, 3, 4, 5, 6],
    },
    {
        "name": "nums2 elements all larger",
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [4, 5, 6],
        "n": 3,
        "expected": [1, 2, 3, 4, 5, 6],
    },
    {
        "name": "Interleaved elements",
        "nums1": [1, 3, 5, 0, 0, 0],
        "m": 3,
        "nums2": [2, 4, 6],
        "n": 3,
        "expected": [1, 2, 3, 4, 5, 6],
    },
    {
        "name": "Duplicate elements",
        "nums1": [1, 3, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 3, 5],
        "n": 3,
        "expected": [1, 2, 3, 3, 3, 5],
    },
    {
        "name": "Negative numbers",
        "nums1": [-5, -1, 3, 0, 0, 0],
        "m": 3,
        "nums2": [-7, 0, 6],
        "n": 3,
        "expected": [-7, -5, -1, 0, 3, 6],
    },
    {
        "name": "Large difference in sizes",
        "nums1": [1, 3, 5, 7, 9, 0],
        "m": 5,
        "nums2": [8],
        "n": 1,
        "expected": [1, 3, 5, 7, 8, 9],
    },
    {
        "name": "nums1 empty, nums2 has all elements",
        "nums1": [0, 0, 0, 0, 0],
        "m": 0,
        "nums2": [1, 2, 3, 4, 5],
        "n": 5,
        "expected": [1, 2, 3, 4, 5],
    },
    {
        "name": "Identical elements",
        "nums1": [2, 2, 2, 0, 0, 0],
        "m": 3,
        "nums2": [2, 2, 2],
        "n": 3,
        "expected": [2, 2, 2, 2, 2, 2],
    },
    {
        "name": "Single element each",
        "nums1": [2, 0],
        "m": 1,
        "nums2": [1],
        "n": 1,
        "expected": [1, 2],
    },
]


@pytest.mark.parametrize("test_case", test_cases, ids=[tc["name"] for tc in test_cases])
def test_merge_sorted_array(test_case):
    Solution().merge(
        test_case["nums1"], test_case["m"], test_case["nums2"], test_case["n"]
    )
    assert test_case["nums1"] == test_case["expected"]
