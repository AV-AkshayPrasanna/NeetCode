class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        d = [float("inf")] * n
        v = [False] * n
        d[0] = 0
        r = 0
        for _ in range(n):
            u = -1
            for i in range(n):
                if not v[i] and (u < 0 or d[i] < d[u]):
                    u = i
            v[u] = True
            r += d[u]
            for i in range(n):
                if not v[i]:
                    d[i] = min(d[i], abs(points[u][0] - points[i][0]) + abs(points[u][1] - points[i][1]))
        return r