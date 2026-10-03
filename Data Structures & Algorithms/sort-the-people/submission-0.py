class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)

        return [name for height, name in people]