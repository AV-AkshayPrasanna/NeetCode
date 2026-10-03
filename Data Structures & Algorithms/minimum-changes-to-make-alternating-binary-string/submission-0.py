class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0

        for i in range(len(s)):
            expected = '0' if i % 2 == 0 else '1'

            if s[i] != expected:
                changes += 1

        return min(changes, len(s) - changes)