class Solution:
    def isSubtree(self, root, subRoot):
        def same(a, b):
            stack = [(a, b)]

            while stack:
                x, y = stack.pop()

                if not x and not y:
                    continue

                if not x or not y or x.val != y.val:
                    return False

                stack.append((x.left, y.left))
                stack.append((x.right, y.right))

            return True

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and same(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False