class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        res = []
        i = 0
        for j in range(1, len(s)):
            if s[j] == '.':
                continue
            gap = j - i - 1  # dots between i and j
            if i > 0:
                res.append(s[i])  # real force at i (skip the virtual 'L')
            if s[i] == s[j]:
                res.append(s[i] * gap)
            elif s[i] == 'L' and s[j] == 'R':
                res.append('.' * gap)
            else:  # s[i] == 'R' and s[j] == 'L'
                half = gap // 2
                res.append('R' * half + '.' * (gap % 2) + 'L' * half)
            i = j
        return ''.join(res)