class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1_i = 0
        nums2_i = 0
        while nums1_i < m + n and n != 0:
            if nums1_i < m:
                if nums1[nums1_i] < nums2[nums2_i]:
                    nums1_i += 1
                    continue

                nums1[nums1_i], nums2[nums2_i] = nums2[nums2_i], nums1[nums1_i]
                nums2.sort()
                nums1_i += 1
                continue

            nums1[nums1_i], nums2[nums2_i] = nums2[nums2_i], nums1[nums1_i]
            nums1_i += 1
            nums2_i += 1
