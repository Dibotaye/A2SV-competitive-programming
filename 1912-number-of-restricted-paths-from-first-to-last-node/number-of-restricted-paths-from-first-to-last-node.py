class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = []
        heapq.heappush(pq, (0, n))

        while pq:
            d,node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for i,w in g[node]:
                if dist[node] + w < dist[i]:
                    dist[i] = dist[node] + w
                    heapq.heappush(pq,(dist[i],i))

        
        dp = [0] * (n + 1)
        dp[n] = 1  

        order = list(range(1,n+1))
        order.sort(key=lambda x: dist[x])

        for u in order:
            for v,w in g[u]:
                if dist[u] > dist[v]:
                    dp[u] = (dp[u] + dp[v]) % (10**9+7)

        return dp[1]




            
            