class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        ans = []
        for idx, item in enumerate(intervals):
            if newInterval[0] >= item[0] and newInterval[0] <= item[1]:
                new_item = [item[0], max(item[1], newInterval[1])]
                ans.append(new_item)
                idx += 1
                while ans and intervals[idx][0] <= ans[-1][1]:
                    new_item = [ans[-1][0], max(ans[-1][1], intervals[idx][1])]
                    ans.pop()
                    ans.append(new_item)
                    idx += 1
                ans += intervals[idx:]
                break
            else:
                ans.append(item)
        return ans