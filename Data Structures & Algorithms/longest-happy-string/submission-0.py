import heapq

class Solution:
    def longestDiverseString(self, a, b, c):
        heap = []

        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                heapq.heappush(heap, (count, char))

        result = []

        while heap:
            count, char = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break

                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1

                if count2:
                    heapq.heappush(heap, (count2, char2))

                heapq.heappush(heap, (count, char))
            else:
                result.append(char)
                count += 1

                if count:
                    heapq.heappush(heap, (count, char))

        return "".join(result)