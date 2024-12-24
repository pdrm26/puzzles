class Solution(object):
    def isPalindrome(self, s):
        lower_s = list(s.lower())
        l_pointer = 0
        r_pointer = -1

        while len(lower_s):
            left_char = lower_s[l_pointer]
            right_char = lower_s[r_pointer]

            if not left_char.isalnum():
                lower_s.pop(l_pointer)
                continue

            if not right_char.isalnum():
                lower_s.pop(r_pointer)
                continue

            if left_char != right_char:
                return False

            if left_char == right_char and len(lower_s) == 1:
                return True

            lower_s.pop(l_pointer)
            lower_s.pop(r_pointer)

        return len(lower_s) == 0
   
