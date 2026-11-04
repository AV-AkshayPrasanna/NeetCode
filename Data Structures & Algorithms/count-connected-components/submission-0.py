class Solution:
    def countComponents(self, n, edges):
        p = list(range(n))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for a, b in edges:
            a, b = f(a), f(b)
            if a != b:
                p[a] = b
                n -= 1
        return n