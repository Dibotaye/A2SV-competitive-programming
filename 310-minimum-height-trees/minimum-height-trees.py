class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        neighbors = [[] for i in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        
        res = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                res.append(i)

        x = n
        while x > 2:
            x -= len(res)
            new = []

            for i in res:
                n = neighbors[i][0]
                neighbors[n].remove(i)   
                if len(neighbors[n]) == 1:
                    new.append(n)

        
            res = new
        return res






            