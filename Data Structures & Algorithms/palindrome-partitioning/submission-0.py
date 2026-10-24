class Solution:
    def partition(self, s):
        r = []
        def f(i, p):
            if i == len(s):
                r.append(p[:])
                return
            for j in range(i + 1, len(s) + 1):
                t = s[i:j]
                if t == t[::-1]:
                    p.append(t)
                    f(j, p)
                    p.pop()
        f(0, [])
        return r