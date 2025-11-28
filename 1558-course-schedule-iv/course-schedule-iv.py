class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [[False] * numCourses for _ in range(numCourses)]

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
            pre[u][v] = True

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()

            for v in adj[u]:
                for x in range(numCourses):
                    if pre[x][u]:
                        pre[x][v] = True

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [pre[u][v] for u, v in queries]
            





            