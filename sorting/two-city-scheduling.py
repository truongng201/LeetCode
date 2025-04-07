class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        refund = []
        for item in costs:
            ans += item[0]
            refund.append(item[1] - item[0])
        refund.sort()
        print(refund)
        for i in range(len(refund)//2):
            ans += refund[i]
        return ans