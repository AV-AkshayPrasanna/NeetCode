from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        return list(common.elements())