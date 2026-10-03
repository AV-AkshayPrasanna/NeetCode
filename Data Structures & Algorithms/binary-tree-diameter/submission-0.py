class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        stack = [(root, False)]
        heights = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)

                diameter = max(diameter, left + right)
                heights[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return diameter