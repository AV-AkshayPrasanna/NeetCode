import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        d = [[float("inf")] * n for _ in range(m)]
        d[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            c, x, y = heapq.heappop(h)
            if x == m - 1 and y == n - 1:
                return c
            if c > d[x][y]:
                continue
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= a < m and 0 <= b < n:
                    t = max(c, abs(heights[a][b] - heights[x][y]))
                    if t < d[a][b]:
                        d[a][b] = t
                        heapq.heappush(h, (t, a, b))
        return 0