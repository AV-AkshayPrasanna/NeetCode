class Solution:
    def islandPerimeter(self, grid):
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    r += 4
                    if i and grid[i-1][j]:
                        r -= 2
                    if j and grid[i][j-1]:
                        r -= 2
        return r