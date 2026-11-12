class Solution:
    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        p = list(range(n))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        m = {}
        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x //= d
                    if d in m:
                        p[f(i)] = f(m[d])
                    else:
                        m[d] = i
                d += 1
            if x > 1:
                if x in m:
                    p[f(i)] = f(m[x])
                else:
                    m[x] = i
        r = f(0)
        return all(f(i) == r for i in range(n))