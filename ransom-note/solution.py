class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            letters[i] = letters.get(i, 0) + 1

        for i in ransomNote:
            if not letters.get(i):
                return False
            letters[i] = letters[i] - 1

        return True