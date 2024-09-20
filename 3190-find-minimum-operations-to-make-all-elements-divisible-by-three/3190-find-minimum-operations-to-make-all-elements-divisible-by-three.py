class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if (nums[i]-1)%3==0:
                count+=1
            elif(nums[i]+1)%3==0:
                count+=1
            else:
                count+=0
        return count
        