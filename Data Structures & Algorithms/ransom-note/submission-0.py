from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for char in ransomNote:
            if count[char] == 0:
                return False

            count[char] -= 1

        return True