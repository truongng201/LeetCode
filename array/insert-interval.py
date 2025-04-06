class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        def isOverlap(item1, item2):
            start1, end1 = item1
            start2, end2 = item2
            if end1 < start2 or end2 < start1:
                return False
            return True
        ans = []
        isSet = False
        for idx, item in enumerate(intervals):
            if isOverlap(newInterval, item):
                start, end = newInterval
                isSet = True
                ans.append([min(start, item[0]), max(end, item[1])])
                idx += 1
                break
            else:
                ans.append(item)
        while idx < len(intervals):
            if ans and isOverlap(ans[-1], intervals[idx]):
                new_item = [min(ans[-1][0], intervals[idx][0]), max(ans[-1][1], intervals[idx][1])]
                ans.pop()
                ans.append(new_item)
            else:
                ans.append(intervals[idx])
            idx += 1
        if not isSet:
            ans.append(newInterval)
        return ans