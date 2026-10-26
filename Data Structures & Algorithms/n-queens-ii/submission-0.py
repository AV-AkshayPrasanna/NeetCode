class Solution:
    def totalNQueens(self, n):
        c = set()
        d1 = set()
        d2 = set()
        def f(i):
            if i == n:
                return 1
            r = 0
            for j in range(n):
                if j in c or i - j in d1 or i + j in d2:
                    continue
                c.add(j)
                d1.add(i - j)
                d2.add(i + j)
                r += f(i + 1)
                c.remove(j)
                d1.remove(i - j)
                d2.remove(i + j)
            return r
        return f(0)