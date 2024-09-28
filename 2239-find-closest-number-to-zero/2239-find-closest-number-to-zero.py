class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min=nums[0]
        for i in nums:
            if abs(i)<abs(min) or (abs(i)==abs(min) and i> min):
                min=i
        return min
            
        