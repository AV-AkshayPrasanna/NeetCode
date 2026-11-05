from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        p = list(range(len(accounts)))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        m = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in m:
                    p[f(i)] = f(m[e])
                else:
                    m[e] = i
        g = defaultdict(set)
        for e, i in m.items():
            g[f(i)].add(e)
        return [[accounts[i][0]] + sorted(s) for i, s in g.items()]