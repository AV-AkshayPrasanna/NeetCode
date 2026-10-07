class Solution:
    def rob(self, root):
        if not root:
            return 0

        stack = [(root, False)]
        dp = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left_rob, left_skip = dp.get(node.left, (0, 0))
                right_rob, right_skip = dp.get(node.right, (0, 0))

                rob = node.val + left_skip + right_skip
                skip = max(left_rob, left_skip) + max(right_rob, right_skip)

                dp[node] = (rob, skip)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max(dp[root])