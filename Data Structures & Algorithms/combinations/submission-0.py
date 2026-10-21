class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            # Chosen k numbers: record a copy of the current combination
            if len(path) == k:
                res.append(path[:])
                return

            # Prune: need (k - len(path)) more numbers, so the last
            # valid start is n - (k - len(path)) + 1
            for x in range(start, n - (k - len(path)) + 2):
                path.append(x)
                backtrack(x + 1)
                path.pop()

        backtrack(1)
        return res