class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        m = {}
        def f(x):
            if x in m:
                return m[x]
            c = Node(x.val)
            m[x] = c
            for y in x.neighbors:
                c.neighbors.append(f(y))
            return c
        return f(node)