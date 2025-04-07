class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = {}
        for item in nums:
            if item not in cnt:
                cnt[item] = 1
            else:
                cnt[item] += 1
        
        for key, value in cnt.items():
            if value % 2 == 1:
                return False
        return True