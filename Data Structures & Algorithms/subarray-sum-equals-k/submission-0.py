class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            result += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return result