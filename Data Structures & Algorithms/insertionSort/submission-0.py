class Solution:
    def insertionSort(self, pairs):
        result = []

        for i in range(len(pairs)):
            j = i

            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1

            result.append(pairs.copy())

        return result