class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return

            for j in range(start, len(candidates)):
                # skip duplicate siblings at this level
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                # sorted, so nothing further can fit
                if candidates[j] > remaining:
                    break

                cur.append(candidates[j])
                dfs(j + 1, remaining - candidates[j])
                cur.pop()

        dfs(0, target)
        return res