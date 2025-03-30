import pytest
from solution import Solution

test_cases = [
    {"nums": [3, 2, 2, 3], "val": 3, "expected_k": 2, "expected_nums": [2, 2]},
    {
        "nums": [0, 1, 2, 2, 3, 0, 4, 2],
        "val": 2,
        "expected_k": 5,
        "expected_nums": [0, 0, 1, 3, 4],
    },
    {"nums": [], "val": 5, "expected_k": 0, "expected_nums": []},
    {"nums": [7, 7, 7, 7], "val": 7, "expected_k": 0, "expected_nums": []},
    {"nums": [1, 2, 3, 4], "val": 5, "expected_k": 4, "expected_nums": [1, 2, 3, 4]},
    {"nums": [5], "val": 5, "expected_k": 0, "expected_nums": []},
    {"nums": [10], "val": 5, "expected_k": 1, "expected_nums": [10]},
]


@pytest.mark.parametrize("test_case", test_cases)
def test_remove_element(test_case):
    k = Solution().removeElement(test_case["nums"], test_case["val"])
    assert k == test_case["expected_k"], (
        f"Expected k={test_case['expected_k']}, got k={k}"
    )
