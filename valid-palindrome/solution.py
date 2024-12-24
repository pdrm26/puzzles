class Solution(object):
    def isPalindrome(self, s):
        l_pointer, r_pointer = 0, len(s) - 1

        while l_pointer < r_pointer:
            left_char = s[l_pointer]
            right_char = s[r_pointer]

            if not left_char.isalnum():
                l_pointer += 1
                continue

            if not right_char.isalnum():
                r_pointer -= 1
                continue

            if left_char.lower() != right_char.lower():
                return False

            l_pointer += 1
            r_pointer -= 1

        return True
