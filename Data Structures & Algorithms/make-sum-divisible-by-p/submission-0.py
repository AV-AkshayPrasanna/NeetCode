class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        prefix = 0
        last = {0: -1}
        result = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - target) % p

            if need in last:
                result = min(result, i - last[need])

            last[prefix] = i

        return result if result < len(nums) else -1