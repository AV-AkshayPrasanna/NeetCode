class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        total = 1 << k
        if n - k + 1 < total:
            return False

        seen = [False] * total
        mask = total - 1
        cur = 0
        count = 0

        for i, ch in enumerate(s):
            cur = ((cur << 1) & mask) | (ord(ch) - ord('0'))
            if i >= k - 1 and not seen[cur]:
                seen[cur] = True
                count += 1
                if count == total:
                    return True
        return False