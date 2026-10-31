class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        def f(s):
            v = set(s)
            st = list(s)
            while st:
                x, y = st.pop()
                for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= a < m and 0 <= b < n and (a, b) not in v and heights[a][b] >= heights[x][y]:
                        v.add((a, b))
                        st.append((a, b))
            return v
        p = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        a = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]
        return [list(x) for x in f(p) & f(a)]