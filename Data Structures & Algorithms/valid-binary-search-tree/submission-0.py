class Solution:
    def isValidBST(self, root):
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, low, high = stack.pop()

            if not (low < node.val < high):
                return False

            if node.left:
                stack.append((node.left, low, node.val))

            if node.right:
                stack.append((node.right, node.val, high))

        return True