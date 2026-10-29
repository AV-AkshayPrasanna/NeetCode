class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        def f(i, j):
            if i < 0 or j < 0 or i == m or j == n or not grid[i][j]:
                return 0
            grid[i][j] = 0
            return 1 + f(i+1, j) + f(i-1, j) + f(i, j+1) + f(i, j-1)
        return max(f(i, j) for i in range(m) for j in range(n))