class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left, i, right = 0, 0, len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1