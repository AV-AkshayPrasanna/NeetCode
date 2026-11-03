class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        p = list(range(n))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for a, b in edges:
            a, b = f(a), f(b)
            if a == b:
                return False
            p[a] = b
        return True