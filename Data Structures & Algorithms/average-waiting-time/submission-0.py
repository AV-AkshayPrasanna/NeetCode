class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_wait = 0

        for arrival, time in customers:
            current_time = max(current_time, arrival) + time
            total_wait += current_time - arrival

        return total_wait / len(customers)