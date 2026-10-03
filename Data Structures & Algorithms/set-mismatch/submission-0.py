class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for num in range(1, len(nums) + 1):
            if num not in seen:
                return [duplicate, num]