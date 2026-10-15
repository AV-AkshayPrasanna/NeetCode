class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            if i >= len(nums) or remaining < 0:
                return

            # choose nums[i] again
            cur.append(nums[i])
            dfs(i, remaining - nums[i])
            cur.pop()

            # skip nums[i]
            dfs(i + 1, remaining)

        dfs(0, target)
        return res