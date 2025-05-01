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
        p = find_max_compatible(jobs, n)
        print(jobs)
        print(p)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], dp[p[i]] + jobs[i - 1][2])
        return dp[n]