from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        g = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            g[a].append(b)
        r = []
        s = ["JFK"]
        while s:
            while g[s[-1]]:
                s.append(g[s[-1]].pop())
            r.append(s.pop())
        return r[::-1]