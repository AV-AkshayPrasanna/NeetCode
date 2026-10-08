class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                result.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                result.append("#")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        stack = [(root, 0)]
        i = 1

        while stack:
            node, state = stack.pop()

            if state == 0:
                if values[i] != "#":
                    node.left = TreeNode(int(values[i]))
                    stack.append((node, 1))
                    stack.append((node.left, 0))
                else:
                    stack.append((node, 1))
                i += 1
            else:
                if values[i] != "#":
                    node.right = TreeNode(int(values[i]))
                    stack.append((node.right, 0))
                i += 1

        return root