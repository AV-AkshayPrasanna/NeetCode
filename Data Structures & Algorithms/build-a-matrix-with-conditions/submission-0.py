from collections import deque

class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def f(e):
            g = [[] for _ in range(k + 1)]
            d = [0] * (k + 1)
            for a, b in e:
                g[a].append(b)
                d[b] += 1
            q = deque(i for i in range(1, k + 1) if not d[i])
            p = {}
            while q:
                u = q.popleft()
                p[u] = len(p)
                for v in g[u]:
                    d[v] -= 1
                    if not d[v]:
                        q.append(v)
            return p if len(p) == k else None
        r = f(rowConditions)
        c = f(colConditions)
        if r is None or c is None:
            return []
        m = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            m[r[i]][c[i]] = i
        return m