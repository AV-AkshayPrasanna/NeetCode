class Solution:
    def removeLeafNodes(self, root, target):
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                if node.left and not node.left.left and not node.left.right and node.left.val == target:
                    node.left = None

                if node.right and not node.right.left and not node.right.right and node.right.val == target:
                    node.right = None
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        if not root.left and not root.right and root.val == target:
            return None

        return root