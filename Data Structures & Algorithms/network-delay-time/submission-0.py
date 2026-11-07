import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        g = [[] for _ in range(n + 1)]
        for u, v, t in times:
            g[u].append((v, t))
        d = {}
        h = [(0, k)]
        while h:
            c, u = heapq.heappop(h)
            if u in d:
                continue
            d[u] = c
            for v, t in g[u]:
                if v not in d:
                    heapq.heappush(h, (c + t, v))
        return max(d.values()) if len(d) == n else -1