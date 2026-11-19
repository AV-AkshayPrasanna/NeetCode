class Solution:
    def longestPalindrome(self, s):
        b = 0
        l = 0
        for i in range(len(s)):
            for a, c in ((i, i), (i, i + 1)):
                while a >= 0 and c < len(s) and s[a] == s[c]:
                    a -= 1
                    c += 1
                if c - a - 1 > l:
                    l = c - a - 1
                    b = a + 1
        return s[b:b + l]