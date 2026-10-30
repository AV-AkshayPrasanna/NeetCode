from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque((i, j) for i in range(m) for j in range(n) if grid[i][j] == 0)
        while q:
            x, y = q.popleft()
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 2147483647:
                    grid[a][b] = grid[x][y] + 1
                    q.append((a, b))