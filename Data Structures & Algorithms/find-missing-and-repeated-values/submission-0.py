class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        count = [0] * (n * n + 1)

        for row in grid:
            for num in row:
                count[num] += 1

        repeated = missing = 0

        for num in range(1, n * n + 1):
            if count[num] == 2:
                repeated = num
            elif count[num] == 0:
                missing = num

        return [repeated, missing]