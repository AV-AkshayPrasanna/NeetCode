from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = Counter(arr)

        for word in arr:
            if count[word] == 1:
                k -= 1

                if k == 0:
                    return word

        return ""