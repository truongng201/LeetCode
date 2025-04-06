class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        arr = []
        start, end = newInterval
        idx = 0
        while idx < len(intervals):
            if intervals[idx][0] >= start:
                intervals.insert(idx, newInterval)
                arr += intervals[idx:]
                break
            arr.append(intervals[idx])
            idx += 1
        else:
            arr.append(newInterval)
        ans = [arr[0]]
        for i in range(1, len(arr)):
            if ans[-1][1] >= arr[i][0]:
                new_item = [ans[-1][0], max(arr[i][1], ans[-1][1])]
                ans.pop()
                ans.append(new_item)
            else:
                ans.append(arr[i])
        return ans