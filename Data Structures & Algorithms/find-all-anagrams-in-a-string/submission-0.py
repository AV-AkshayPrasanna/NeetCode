from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        need = [0] * 26
        win = [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1

        matches = sum(1 for c in range(26) if need[c] == win[c])  # starts at 26 - distinct letters in p
        res = []

        def add(c, delta):
            nonlocal matches
            if win[c] == need[c]:
                matches -= 1
            win[c] += delta
            if win[c] == need[c]:
                matches += 1

        for i in range(n):
            add(ord(s[i]) - 97, 1)
            if i >= m:
                add(ord(s[i - m]) - 97, -1)
            if i >= m - 1 and matches == 26:
                res.append(i - m + 1)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("baca", "ac"))   # [1, 2]
    print(sol.findAnagrams("aaaa", "aa"))   # [0, 1, 2]
    print(sol.findAnagrams("ab", "abc"))    # []