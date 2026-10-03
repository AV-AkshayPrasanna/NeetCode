class Solution:
    def isBalanced(self, root):
        heights = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)

                if abs(left - right) > 1:
                    return False

                heights[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return True