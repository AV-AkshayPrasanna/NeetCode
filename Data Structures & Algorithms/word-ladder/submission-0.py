from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        w = set(wordList)
        if endWord not in w:
            return 0
        q = deque([(beginWord, 1)])
        v = {beginWord}
        while q:
            s, k = q.popleft()
            if s == endWord:
                return k
            for i in range(len(s)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    t = s[:i] + c + s[i+1:]
                    if t in w and t not in v:
                        v.add(t)
                        q.append((t, k + 1))
        return 0