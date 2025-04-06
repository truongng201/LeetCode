import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        pq = []
        ans = 0
        for item in intervals:
            start, finish = item
            if pq and pq[0][0] < start: 
                ans -= 1
                heapq.heappop(pq)
            heapq.heappush(pq, (finish, start))
            ans += 1           
        return ans