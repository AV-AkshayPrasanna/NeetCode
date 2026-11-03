class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        n = numCourses
        d = [[False] * n for _ in range(n)]
        for a, b in prerequisites:
            d[a][b] = True
        for k in range(n):
            for i in range(n):
                if d[i][k]:
                    for j in range(n):
                        if d[k][j]:
                            d[i][j] = True
        return [d[u][v] for u, v in queries]