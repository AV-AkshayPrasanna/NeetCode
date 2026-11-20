class Solution:
    def countSubstrings(self, s):
        r = 0
        n = len(s)
        for i in range(n):
            for a, b in ((i, i), (i, i + 1)):
                while a >= 0 and b < n and s[a] == s[b]:
                    r += 1
                    a -= 1
                    b += 1
        return r