class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        for ch in set(s):
            first = s.find(ch)
            last = s.rfind(ch)

            if first < last:
                result += len(set(s[first + 1:last]))

        return result