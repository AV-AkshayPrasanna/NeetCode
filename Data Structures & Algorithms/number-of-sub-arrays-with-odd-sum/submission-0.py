class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        prefix = 0
        result = 0

        for num in arr:
            prefix = (prefix + num) % 2

            if prefix == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

        return result % MOD