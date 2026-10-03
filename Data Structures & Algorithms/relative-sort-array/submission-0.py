class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = {}

        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        remaining = sorted(count.keys())

        for num in remaining:
            result.extend([num] * count[num])

        return result