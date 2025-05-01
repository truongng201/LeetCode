class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        jobs = len(rides)
        for i in range(jobs):
            rides[i][2] += rides[i][1] - rides[i][0]
        
        rides.sort(key=lambda x:x[1])

        def find_max_compatible(jobs, total):
            p = [0] * (total + 1)
            for i in range(2, total + 1):
                start = 0
                end = i - 1
                while start <= end:
                    mid = (start + end) // 2
                    if jobs[mid][1] <= jobs[i - 1][0]:
                        if mid == i - 2 or jobs[mid + 1][1] > jobs[i - 1][0]:
                            p[i] = mid + 1
                            break
                        else:
                            start = mid + 1
                    else:
                        end = mid - 1
            return p
        p = find_max_compatible(rides, jobs)
        dp = [0] * (jobs + 1)
        for i in range(1, jobs + 1):
            dp[i] = max(dp[i - 1], dp[p[i]] + rides[i - 1][2])
        return dp[jobs]