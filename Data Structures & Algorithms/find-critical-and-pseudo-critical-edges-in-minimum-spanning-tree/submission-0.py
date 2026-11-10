class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        e = sorted(range(len(edges)), key=lambda i: edges[i][2])
        def f(s, c):
            p = list(range(n))
            def g(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x
            w = k = 0
            if c >= 0:
                a, b, t = edges[c]
                p[g(a)] = g(b)
                w += t
                k += 1
            for i in e:
                if i == s:
                    continue
                a, b, t = edges[i]
                a, b = g(a), g(b)
                if a != b:
                    p[a] = b
                    w += t
                    k += 1
            return w if k == n - 1 else float("inf")
        m = f(-1, -1)
        x, y = [], []
        for i in range(len(edges)):
            if f(i, -1) > m:
                x.append(i)
            elif f(-1, i) == m:
                y.append(i)
        return [x, y]