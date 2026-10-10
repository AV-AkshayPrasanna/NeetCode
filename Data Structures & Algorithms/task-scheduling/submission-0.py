from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks).values()
        max_freq = max(counts)
        max_count = sum(freq == max_freq for freq in counts)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)