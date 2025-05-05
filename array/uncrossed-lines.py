class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len_1, len_2 = len(nums1), len(nums2)

        dp = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]

        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len_1][len_2]
