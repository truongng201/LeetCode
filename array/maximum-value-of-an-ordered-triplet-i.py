class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_item = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    max_item = max((nums[i] - nums[j]) * nums[k], max_item)
        return max_item