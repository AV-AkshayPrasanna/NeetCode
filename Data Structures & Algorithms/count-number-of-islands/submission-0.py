class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        def f(i, j):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            f(i+1, j)
            f(i-1, j)
            f(i, j+1)
            f(i, j-1)
        r = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    r += 1
                    f(i, j)
        return r