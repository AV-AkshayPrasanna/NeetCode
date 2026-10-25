class Solution:
    def canPartitionKSubsets(self, nums, k):
        t = sum(nums)
        if t % k:
            return False
        s = t // k
        m = sorted(nums, reverse=True)
        if m[0] > s:
            return False
        a = [0] * k
        def f(i):
            if i == len(m):
                return True
            for j in range(k):
                if a[j] + m[i] <= s:
                    a[j] += m[i]
                    if f(i + 1):
                        return True
                    a[j] -= m[i]
                if a[j] == 0:
                    break
            return False
        return f(0)