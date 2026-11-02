from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        d = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            d[a] += 1
        q = deque(i for i in range(numCourses) if not d[i])
        c = 0
        while q:
            u = q.popleft()
            c += 1
            for v in g[u]:
                d[v] -= 1
                if not d[v]:
                    q.append(v)
        return c == numCourses