class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        n = len(startTime)
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x:x[1])

        def find_max_compatible(jobs, total_job):
            p = [0] * (total_job + 1)

            for i in range(2, total_job + 1):
                start = 0
                end = i - 1
                while start < end:
                    if jobs[start][1] <= jobs[i - 1][0]:
                        p[i] = start + 1
                        start += 1
                    else:
                        break
            return p
        p = find_max_compatible(jobs, n)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], dp[p[i]] + jobs[i - 1][2])
        return dp[n]