class Solution:
    def makesquare(self, matchsticks):
        t = sum(matchsticks)
        if t % 4:
            return False
        s = t // 4
        m = sorted(matchsticks, reverse=True)
        if m[0] > s:
            return False
        a = [0] * 4
        def f(i):
            if i == len(m):
                return True
            for j in range(4):
                if a[j] + m[i] <= s:
                    a[j] += m[i]
                    if f(i + 1):
                        return True
                    a[j] -= m[i]
                if a[j] == 0:
                    break
            return False
        return f(0)