from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        g = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1 / v
        def f(a, b):
            if a not in g or b not in g:
                return -1.0
            s = [(a, 1.0)]
            v = {a}
            while s:
                x, r = s.pop()
                if x == b:
                    return r
                for y, w in g[x].items():
                    if y not in v:
                        v.add(y)
                        s.append((y, r * w))
            return -1.0
        return [f(a, b) for a, b in queries]