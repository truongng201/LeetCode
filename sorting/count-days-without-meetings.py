class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meet = [False] * (days + 1)
        print(meet)
        for meeting in meetings:
            for i in range(meeting[0], meeting[1] + 1):
                meet[i] = True
        cnt = 0
        for i in range(1, days + 1):
            if not meet[i]:
                cnt += 1
        return cnt