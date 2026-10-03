class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area