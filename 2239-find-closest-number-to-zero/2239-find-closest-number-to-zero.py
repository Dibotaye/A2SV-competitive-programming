class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        j=nums[0]
        for i in nums:
            if (abs(i)<abs(j)) or (abs(i)==abs(j) and i>j):
                j=i
        return j
                
        