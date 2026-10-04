class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            result.append(queue[-1].val)
            next_queue = []

            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue

        return result