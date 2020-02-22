import sys


class Solution:
    def a(self, days: List[int], costs: List[int]) -> int:
        if(len(days) == 0):
            return 0

        if(days[0]):
            min_val = sys.maxsize
            mincostSmall = self.a(days[1:], costs) + costs[0]
            min_val = min(min_val, mincostSmall)
            mincostSmall = self.a(days[7:], costs) + costs[1]
            min_val = min(min_val, mincostSmall)
            mincostSmall = self.a(days[30:], costs) + costs[2]
            min_val = min(min_val, mincostSmall)
            return min_val

        else:
            return self.a(days[1:], costs)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        boolDays = [False] * 366
        for day in days:
            boolDays[day] = True
        return self.a(boolDays[1:], costs)
