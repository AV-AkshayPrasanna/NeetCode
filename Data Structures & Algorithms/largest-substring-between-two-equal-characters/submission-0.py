class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, char in enumerate(s):
            if char in first:
                ans = max(ans, i - first[char] - 1)
            else:
                first[char] = i

        return ans