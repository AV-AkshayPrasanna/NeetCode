from collections import Counter

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = Counter("".join(words))
        n = len(words)

        return all(freq % n == 0 for freq in count.values())