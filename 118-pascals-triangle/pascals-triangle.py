class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    x = arr[i-1][j-1] + arr[i-1][j]
                    row.append(x)
            arr.append(row)

        return arr