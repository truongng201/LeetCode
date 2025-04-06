class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans and intervals[i][0] <= ans[-1][1]:
                new_interval = [ans[-1][0], intervals[i][1]]
                ans.pop()
                ans.append(new_interval)
                continue
            ans.append(intervals[i])
        return ans