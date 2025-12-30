class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def helper(x):
            left_len = index
            if x > left_len:
                left_sum = (x-1+x - left_len) * left_len // 2
            else:
                left_sum = (x-1+1) * (x-1) // 2 + (left_len - (x-1))

            
            right_len = n-index-1
            if x > right_len:
                right_sum = (x -1 + x - right_len) * right_len // 2
            else:
                right_sum = (x - 1 + 1) * (x - 1) // 2 + (right_len - (x - 1))

            return left_sum + x + right_sum

        l = 1 
        h = maxSum
        ans = 1

        while l <= h:
            mid = (l+h) // 2
            if helper(mid) <= maxSum:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans


