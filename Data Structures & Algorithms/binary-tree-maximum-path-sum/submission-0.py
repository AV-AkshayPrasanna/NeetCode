class Solution:
    def maxPathSum(self, root):
        stack = [(root, False)]
        gain = {}
        result = float('-inf')

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left = max(0, gain.get(node.left, 0))
                right = max(0, gain.get(node.right, 0))

                result = max(result, node.val + left + right)
                gain[node] = node.val + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result