class Solution:
    def numDecodings(self, s):
        a, b = 0, 1
        for i in range(len(s)):
            c = 0
            if s[i] != "0":
                c += b
            if i and "10" <= s[i-1:i+1] <= "26":
                c += a
            a, b = b, c
        return b