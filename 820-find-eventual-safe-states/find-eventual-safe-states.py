class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    
        mapp = {}

        def dfs(i):
            if i in mapp:
                return mapp[i]
            mapp[i] = False
            for n in graph[i]:
                if not dfs(n):
                    return mapp[i]
            mapp[i] = True
            return mapp[i]


        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res



            