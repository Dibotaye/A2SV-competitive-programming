class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.count = n
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
            self.count -= 1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        dsu = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                count = 0
                for k in range(len(strs[i])):
                    # count = 0
                    if strs[i][k] != strs[j][k]:
                        count+= 1
                if count <= 2:
                    dsu.union(i,j)

        return dsu.count
        