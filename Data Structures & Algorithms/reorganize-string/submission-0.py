import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s):
        freq = Counter(s)

        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_count, prev_char = 0, ""

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            count += 1
            prev_count, prev_char = count, char

        return "".join(result)