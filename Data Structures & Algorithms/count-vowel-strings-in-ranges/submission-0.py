class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        prefix = [0]

        for word in words:
            prefix.append(prefix[-1] + (word[0] in vowels and word[-1] in vowels))

        return [prefix[r + 1] - prefix[l] for l, r in queries]