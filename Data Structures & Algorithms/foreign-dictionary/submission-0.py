from collections import deque

class Solution:
    def foreignDictionary(self, words):
        g = {c: set() for w in words for c in w}
        d = {c: 0 for c in g}
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            if len(a) > len(b) and a[:len(b)] == b:
                return ""
            for x, y in zip(a, b):
                if x != y:
                    if y not in g[x]:
                        g[x].add(y)
                        d[y] += 1
                    break
        q = deque(c for c in d if not d[c])
        r = []
        while q:
            u = q.popleft()
            r.append(u)
            for v in g[u]:
                d[v] -= 1
                if not d[v]:
                    q.append(v)
        return "".join(r) if len(r) == len(g) else ""