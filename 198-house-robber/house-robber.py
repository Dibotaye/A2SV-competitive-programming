class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}


        def dp(index):

            if index == len(nums)-1:
                return nums[index]
            
            if index == len(nums)-2:
                return max(nums[index + 1], nums[index])

            if index not in memo:
                memo[index] = max(dp(index + 1), dp(index + 2) + nums[index])
            return memo[index]
        
        return dp(0)


        

