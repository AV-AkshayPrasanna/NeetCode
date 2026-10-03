from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        max_odd = max(count for count in freq.values() if count % 2 == 1)
        min_even = min(count for count in freq.values() if count % 2 == 0)

        return max_odd - min_even