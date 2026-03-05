class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        for j in range(1,n):
            ones = 0
            for i in range(m):
                if grid[i][j] == 1:
                    ones += 1

            zeros = m - ones
            if zeros > ones:
                for i in range(m):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        score = 0
        for i in range(m):
            value = 0
            for j in range(n):
                value = value * 2+grid[i][j]
            score += value

        return score
                