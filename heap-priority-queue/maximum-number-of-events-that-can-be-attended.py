class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[1])
        curr_day = 1
        for event in events:
            if event[0] <= curr_day and event[1] >= curr_day:
                curr_day += 1
        return curr_day - 1