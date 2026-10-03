import heapq

class Solution:
    def shortestPath(self, n, edges, src):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        distances = [float("inf")] * n
        distances[src] = 0

        min_heap = [(0, src)]

        while min_heap:
            current_dist, node = heapq.heappop(min_heap)

            if current_dist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = current_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        result = {}

        for i in range(n):
            if distances[i] == float("inf"):
                result[i] = -1
            else:
                result[i] = distances[i]

        return result