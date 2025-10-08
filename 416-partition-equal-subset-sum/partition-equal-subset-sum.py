class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}

        def dp(i,summ):
            if i == len(nums):
                return summ == 0

            s = (i,summ)
            if s not in memo:
                memo[s] = dp(i+1,summ -nums[i]) or dp(i+1,summ)
            return memo[s]
        
        half = sum(nums)//2
        
        return sum(nums)%2 == 0 and dp(0,half)





        