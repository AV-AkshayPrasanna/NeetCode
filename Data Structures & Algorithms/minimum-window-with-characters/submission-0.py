class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1

        have = 0
        need = len(count)
        window = {}

        left = 0
        best_len = float('inf')
        best_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count and window[char] == count[char]:
                have += 1

            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in count and window[left_char] < count[left_char]:
                    have -= 1

                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]