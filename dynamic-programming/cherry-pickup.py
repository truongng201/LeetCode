from collections import deque
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[0, 0] for _ in range(n)]  for _ in range(n)] 
        q = deque()
        q.append([0, 0, True])
        while q:
            curr_node = q.popleft()
            curr_x, curr_y, is_first = curr_node
            
            if is_first:
                dp[curr_x][curr_y][0] = grid[curr_x][curr_y] + max(dp[max(curr_x - 1, 0)][curr_y][0], dp[curr_x][max(curr_y - 1, 0)][0])
                dp[curr_x][curr_y][1] =  max(dp[max(curr_x - 1, 0)][curr_y][1], dp[curr_x][max(curr_y - 1, 0)][1])
            else:
                dp[curr_x][curr_y][0] =  max(dp[max(curr_x - 1, 0)][curr_y][0], dp[curr_x][max(curr_y - 1, 0)][0])
                dp[curr_x][curr_y][1] = grid[curr_x][curr_y] + max(dp[max(curr_x - 1, 0)][curr_y][1], dp[curr_x][max(curr_y - 1, 0)][1])
            
            directions = [[1, 0], [0, 1]]
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                
                if new_x >= n or new_y >= n:
                    continue
                
                if grid[new_x][new_y] == -1:
                    dp[new_x][new_y] = [0, 0]
                    continue
                
                q.append([new_x, new_y, is_first])
                is_first = not is_first
                
        return dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1]
