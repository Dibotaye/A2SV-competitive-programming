class Solution:
    def pivotInteger(self, n: int) -> int:
        num=list(range(n+1))
        for i in range(len(num)):
            if sum(num[:i])==sum(num[i+1:]):
                return i
        return -1
        