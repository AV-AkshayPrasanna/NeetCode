from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        d = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            d[a] += 1
        q = deque(i for i in range(numCourses) if not d[i])
        r = []
        while q:
            u = q.popleft()
            r.append(u)
            for v in g[u]:
                d[v] -= 1
                if not d[v]:
                    q.append(v)
        return r if len(r) == numCourses else []