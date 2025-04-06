class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        cnt = 0
        meetings.sort(key=lambda x:x[0])
        curr = meetings[0]
        for i in range(1, len(meetings)):
            if meetings[i][0] > curr[1]:
                cnt += meetings[i][0] - curr[1] - 1
            curr = meetings[i]
        if curr[1] < days:
            cnt += days - curr[1]
        return cnt