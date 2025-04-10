import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for item in roads:
            graph[item[0]].append((item[1], item[2]))
            graph[item[1]].append((item[0], item[2]))
        cnt = [0 for _ in range(n)]
        min_dist = [float("inf") for _ in range(n)]
        visited = [False] * (n + 1)
        pq = []
        heapq.heappush(pq, (0, 0))
        while pq:
            curr_val = heapq.heappop(pq)
            curr_weight, curr_node = curr_val
            print(cnt, curr_node, curr_weight)
            if visited[curr_node]:
                continue
            visited[curr_node] = True

            for neighbor in graph.get(curr_node):
                neighbor_node, neighbor_weight = neighbor
                if neighbor_weight + curr_weight < min_dist[neighbor_node]:
                    heapq.heappush(pq, (neighbor_weight + curr_weight, neighbor_node))
                    min_dist[neighbor_node] = neighbor_weight + curr_weight
                    cnt[neighbor_node] = 1
                elif neighbor_weight + curr_weight == min_dist[neighbor_node]:
                    cnt[neighbor_node] += cnt[curr_node]
        return cnt[n - 1]