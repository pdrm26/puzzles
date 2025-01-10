class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        second_index = 1
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    first_index = i
                    second_index = j
                    break

            if nums[first_index] + nums[second_index] == target:
                break

        return [first_index, second_index]
