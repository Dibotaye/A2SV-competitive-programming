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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dsu = UnionFind(m*n+1)


        dummy = m*n 

 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in (0, m - 1) or j in (0, n - 1):
                        dsu.union(i*n+j,dummy)

        
        dxn= [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for dx,dy in dxn:
                        ni= i + dx
                        nj =  j + dy
                        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                            dsu.union(i*n+ j, ni*n+ nj)



        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if dsu.find(i*n+ j) != dsu.find(dummy):
                        board[i][j] = 'X'








