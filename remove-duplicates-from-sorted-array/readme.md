# 26. Remove Duplicates from Sorted Array

**Solved**  
**Difficulty:** Easy

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears **only once**. The relative order of the elements should be kept the same. Then return the **number of unique elements** in `nums`.

Consider the number of unique elements in `nums` to be `k`. To get accepted, you need to do the following:

1. Modify the array `nums` so that the first `k` elements contain the unique elements in their original order.
2. The remaining elements in `nums` **do not matter**.
3. Return `k`.

---

## Custom Judge

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
