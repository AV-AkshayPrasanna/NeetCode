import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        v = [[False] * n for _ in range(n)]
        h = [(grid[0][0], 0, 0)]
        v[0][0] = True
        while h:
            t, x, y = heapq.heappop(h)
            if x == n - 1 and y == n - 1:
                return t
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= a < n and 0 <= b < n and not v[a][b]:
                    v[a][b] = True
                    heapq.heappush(h, (max(t, grid[a][b]), a, b))