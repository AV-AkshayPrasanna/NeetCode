class Solution:
    def goodNodes(self, root):
        count = 0
        stack = [(root, root.val)]

        while stack:
            node, max_val = stack.pop()

            if node.val >= max_val:
                count += 1
                max_val = node.val

            if node.left:
                stack.append((node.left, max_val))

            if node.right:
                stack.append((node.right, max_val))

        return count