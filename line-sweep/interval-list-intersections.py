class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        combine = []
        i, j = 0, 0
        while i < len(firstList) or j < len(secondList):
            if j >= len(secondList):
                combine += firstList[i:]
                break
            if i >= len(firstList):
                combine += secondList[j:]
                break
            if firstList[i][0] < secondList[j][0]:
                combine.append(firstList[i])
                i += 1
            else:
                combine.append(secondList[j])
                j += 1
        def get_overlap(item1, item2):
            f1, s1 = item1
            f2, s2 = item2
            if s1 < f2 or s2 < f1:
                return []
            return [max(f1, f2), min(s1, s2)]
        ans = []
        for i in range(1, len(combine)):
            x = get_overlap(combine[i], combine[i-1])
            if len(x) != 0:
                ans.append(x)
        return ans