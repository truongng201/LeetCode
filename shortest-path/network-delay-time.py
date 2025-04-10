import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n + 1)}
        for item in times:
            graph[item[0]].append((item[1], item[2]))
        
        distance = [float("inf") for i in range(n + 1)]
        visited = [False] * (n + 1)
        pq = []
        heapq.heappush(pq, (0, k))
        ans = 0
        while pq:
            curr_val = heapq.heappop(pq)
            curr_weight, curr_node = curr_val
            if visited[curr_node]:
                continue
            visited[curr_node] = True
            distance[curr_node] = curr_weight
            ans = max(ans, curr_weight)

            for neighbor in graph[curr_node]:
                neighbor_node, neighbor_weight = neighbor
                if neighbor_weight + curr_weight < distance[neighbor_node]:
                    heapq.heappush(pq, (neighbor_weight + curr_weight, neighbor_node))
        for i in range(1, n+1):
            if distance[i] == float("inf"):
                return -1
        return ans

