class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        res = [set() for _ in range(n)]

        while queue:
            curr = queue.popleft()

            for i in graph[curr]:
                res[i].add(curr)

                
                for x in res[curr]:
                    res[i].add(x)

                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)


        result = []
        for i in range(n):
            result.append(sorted(list(res[i])))

        return result


                