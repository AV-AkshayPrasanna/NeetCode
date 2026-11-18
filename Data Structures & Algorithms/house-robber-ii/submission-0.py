class Solution:
    def rob(self, nums):
        def f(a):
            x = y = 0
            for v in a:
                x, y = y, max(y, x + v)
            return y
        return max(nums[0], f(nums[1:]), f(nums[:-1]))