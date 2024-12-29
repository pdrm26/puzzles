from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_phrases: List[str] = []
        min_len_str = strs[0]

        for s in strs:
            if len(s) < len(min_len_str):
                min_len_str = s

        for i in range(len(min_len_str)):

            match = True
            for word in strs:
                if word[i] != min_len_str[i]:
                    match = False
                    break

            if match:
                common_phrases.append(min_len_str[i])

        if not common_phrases:
            return ''

        return "".join(common_phrases)


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
