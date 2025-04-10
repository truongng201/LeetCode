class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(visited, graph, node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(visited, graph, neighbor)

        graph = {i: [] for i in range(n)}
        for item in connections:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])

        visited = [False] * n
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(visited, graph, i)
                components += 1
        if len(connections) < n - 1:
            return -1
        return components - 1