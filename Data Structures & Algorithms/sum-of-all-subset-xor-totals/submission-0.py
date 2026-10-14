class Solution:
    def subsetXORSum(self, nums):
        result = 0

        def dfs(i, xor_total):
            nonlocal result

            if i == len(nums):
                result += xor_total
                return

            dfs(i + 1, xor_total)
            dfs(i + 1, xor_total ^ nums[i])

        dfs(0, 0)
        return result