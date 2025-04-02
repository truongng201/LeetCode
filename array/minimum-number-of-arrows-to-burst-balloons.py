class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt = 0
        points.sort(key=lambda x:x[1])
        last_end = points[0][1]
        print(points)
        for i in range(1, len(points)):
            if points[i][0] > last_end:
                cnt += 1
                last_end = points[i][1]
        cnt += 1
        return cnt