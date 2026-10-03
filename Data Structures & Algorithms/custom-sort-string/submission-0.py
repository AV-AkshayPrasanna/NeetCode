from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []

        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]

        for char, freq in count.items():
            result.append(char * freq)

        return "".join(result)