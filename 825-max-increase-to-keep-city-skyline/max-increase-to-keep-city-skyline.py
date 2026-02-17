class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0]*n
        col = [0]*n
        
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                row[r] = max(row[r], grid[r][c])
                col[c] = max(col[c], grid[r][c])


        res = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                res += max(min(row[r], col[c]) - grid[r][c], 0)
        return res


