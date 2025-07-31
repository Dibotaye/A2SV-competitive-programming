class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 != root2:
            self.parent[root2] = root1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind(len(accounts))
        mapemail = {}

        for i, v in enumerate(accounts):
            for j in v[1:]:
                if j in mapemail:
                    dsu.union(mapemail[j],i)
                else:
                    mapemail[j] = i

    
        emailgroup = defaultdict(list)
        for i, v in mapemail.items():
            x = dsu.find(v)
            emailgroup[x].append(i)
        ans =[]
        for i, e in emailgroup.items():
            name = accounts[i][0]
            y = sorted(emailgroup[i])
            ans.append([name]+ y)
        return ans
        
            

        

        