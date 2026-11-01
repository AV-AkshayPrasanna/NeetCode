from collections import deque

class Solution:
    def openLock(self, deadends, target):
        d = set(deadends)
        if "0000" in d:
            return -1
        v = {"0000"}
        q = deque([("0000", 0)])
        while q:
            s, k = q.popleft()
            if s == target:
                return k
            for i in range(4):
                for x in (1, 9):
                    t = s[:i] + str((int(s[i]) + x) % 10) + s[i+1:]
                    if t not in v and t not in d:
                        v.add(t)
                        q.append((t, k + 1))
        return -1