class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        d = [float("inf")] * n
        d[src] = 0
        for _ in range(k + 1):
            t = d[:]
            for a, b, c in flights:
                if d[a] + c < t[b]:
                    t[b] = d[a] + c
            d = t
        return -1 if d[dst] == float("inf") else d[dst]