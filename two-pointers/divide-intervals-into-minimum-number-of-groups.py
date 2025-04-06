class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        resources = []
        ans = 0
        for item in intervals:
            ans = max(ans, len(resources))
            start, finish = item
            i = 0
            con = False
            while i < len(resources):
                if resources[i][1] < start:
                    resources[i] = item
                    break
                i += 1
            else:
                resources.append(item)
        ans = max(ans, len(resources))
        return ans