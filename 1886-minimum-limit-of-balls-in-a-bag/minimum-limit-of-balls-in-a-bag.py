class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        

        def helper(x):
            oper = 0
            for i in nums:
                oper += (i-1) //x
            return oper <= maxOperations
        
        l = 1
        r = max(nums)
        while l < r:
            mid = (l+r) // 2
            if helper(mid):
                r = mid
            else:
                l = mid + 1

        return l



        