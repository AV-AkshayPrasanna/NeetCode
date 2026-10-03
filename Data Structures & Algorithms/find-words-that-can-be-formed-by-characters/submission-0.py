from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = Counter(chars)
        total = 0

        for word in words:
            freq = Counter(word)

            if all(freq[ch] <= available[ch] for ch in freq):
                total += len(word)

        return total