class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        ans = []
        if intervals[0][0] > newInterval[0]:
            ans.append([min(intervals[0][0], newInterval[0]), max(intervals[0][1], newInterval[1])])
            if len(intervals) > 1:
                ans += intervals[1:]
            return ans
        for idx, item in enumerate(intervals):
            if newInterval[0] >= item[0] and newInterval[0] <= item[1]:
                new_item = [item[0], max(item[1], newInterval[1])]
                ans.append(new_item)
                idx += 1
                while ans and idx < len(intervals) and intervals[idx][0] <= ans[-1][1]:
                    new_item = [ans[-1][0], max(ans[-1][1], intervals[idx][1])]
                    ans.pop()
                    ans.append(new_item)
                    idx += 1
                ans += intervals[idx:]
                return ans
            else:
                ans.append(item)
        ans.append(newInterval)
        return ans