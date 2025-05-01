class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0]*(n + 1)
        
        for i in range(1, n + 1):
            for j in range(0, i):
                if nums[i - 1] > nums[j]:
                    dp[i] = max(dp[i], dp[j + 1])
            dp[i] += 1
            print(dp)
        return max(dp)
