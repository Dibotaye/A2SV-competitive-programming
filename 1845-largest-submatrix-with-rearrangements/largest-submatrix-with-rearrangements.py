class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        ans = 0
        for i in matrix:
            i.sort()
            i.reverse()
            for j in range(n):
                ans = max(ans,i[j]*(j+1))

        return ans


            