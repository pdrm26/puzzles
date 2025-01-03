class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        first_index = 0

        while first_index < len(haystack):
            if haystack[first_index:first_index + len(needle)] == needle:
                return first_index
            first_index += 1

        return -1
