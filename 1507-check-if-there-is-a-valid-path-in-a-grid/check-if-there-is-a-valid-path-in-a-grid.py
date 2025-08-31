class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n)]
    def find(self,x):
        if self.parent[x] == x:
            return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 != root2:
            self.parent[root2] = root1

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dsu = UnionFind(len(grid)*len(grid[0]))
        dxn = {1: [(0, -1), (0, 1)], 2: [(-1, 0), (1, 0)],3: [(0, -1), (1, 0)],   4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)],6: [(0, 1), (-1, 0)],}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for dx,dy in dxn[grid[i][j]]:
                    ni= i + dx
                    nj = j + dy
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if (-dx, -dy) in dxn[grid[ni][nj]]:
                            
                            dsu.union(i*len(grid[0]) + j, ni*len(grid[0]) + nj)


        return dsu.find(0) == dsu.find(len(grid)*len(grid[0]) - 1)

        