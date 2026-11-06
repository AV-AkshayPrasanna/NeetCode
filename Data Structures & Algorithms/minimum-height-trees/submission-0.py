class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        l = [i for i in range(n) if len(g[i]) == 1]
        while n > 2:
            n -= len(l)
            t = []
            for u in l:
                v = g[u].pop()
                g[v].remove(u)
                if len(g[v]) == 1:
                    t.append(v)
            l = t
        return l