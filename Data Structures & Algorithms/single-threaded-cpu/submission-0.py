import heapq

class Solution:
    def getOrder(self, tasks):
        sorted_tasks = sorted(
            (enqueue, process, i)
            for i, (enqueue, process) in enumerate(tasks)
        )

        heap = []
        result = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                enqueue, process, idx = sorted_tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            process, idx = heapq.heappop(heap)
            time += process
            result.append(idx)

        return result