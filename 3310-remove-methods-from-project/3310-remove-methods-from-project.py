class Solution:
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nxt in graph[node]:
                if not suspicious[nxt]:
                    dfs(nxt)

        dfs(k)

        for u, v in invocations:
            if (not suspicious[u]) and suspicious[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans