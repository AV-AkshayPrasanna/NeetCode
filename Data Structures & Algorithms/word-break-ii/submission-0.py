class Solution:
    def wordBreak(self, s, wordDict):
        w = set(wordDict)
        r = []
        def f(i, p):
            if i == len(s):
                r.append(" ".join(p))
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in w:
                    p.append(s[i:j])
                    f(j, p)
                    p.pop()
        f(0, [])
        return r