class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x:x[0])
        curr = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i][0] <= curr[1]:
                curr = [min(curr[0], nums[i][0]), max(curr[1], nums[i][1])]
            else:
                cnt += curr[1] - curr[0] + 1
                curr = nums[i]
        return cnt + curr[1] - curr[0] + 1