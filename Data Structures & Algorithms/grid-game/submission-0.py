from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = sum(grid[0])  # will become sum of grid[0][k+1:]
        bottom = 0          # sum of grid[1][:k]
        ans = float("inf")

        for k in range(n):
            top -= grid[0][k]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][k]

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.gridGame([[1, 4, 2], [3, 2, 1]]))  # 3
    print(sol.gridGame([[5], [7]]))              # 0
    print(sol.gridGame([[1, 1], [9, 1]]))        # 1