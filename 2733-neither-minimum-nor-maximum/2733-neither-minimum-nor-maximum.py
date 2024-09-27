class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in nums:
            if i !=min(nums) and i !=max(nums):
                return i
        return -1
        