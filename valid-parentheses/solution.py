class Solution(object):
    def isValid(self, s):
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in list(s):
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
