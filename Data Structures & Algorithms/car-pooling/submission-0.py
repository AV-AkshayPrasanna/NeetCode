class Solution:
    def carPooling(self, trips, capacity):
        locations = [0] * 1001

        for passengers, start, end in trips:
            locations[start] += passengers
            locations[end] -= passengers

        current = 0

        for change in locations:
            current += change
            if current > capacity:
                return False

        return True