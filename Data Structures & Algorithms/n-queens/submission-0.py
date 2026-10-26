class Solution:
    def solveNQueens(self, n):
        r = []
        c = set()
        d1 = set()
        d2 = set()
        p = []
        def f(i):
            if i == n:
                r.append(["." * j + "Q" + "." * (n - j - 1) for j in p])
                return
            for j in range(n):
                if j in c or i - j in d1 or i + j in d2:
                    continue
                c.add(j)
                d1.add(i - j)
                d2.add(i + j)
                p.append(j)
                f(i + 1)
                p.pop()
                c.remove(j)
                d1.remove(i - j)
                d2.remove(i + j)
        f(0)
        return r