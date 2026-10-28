class Solution:
    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        a = [[m[c] for c in w] for w in words]
        return all(a[i] <= a[i + 1] for i in range(len(a) - 1))