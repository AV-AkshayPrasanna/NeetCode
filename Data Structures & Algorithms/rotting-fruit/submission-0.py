from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    f += 1
        t = 0
        while q:
            x, y, t = q.popleft()
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                    grid[a][b] = 2
                    f -= 1
                    q.append((a, b, t + 1))
        return -1 if f else t