class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() 
        x = nums[0]
        count = 1  
        for i in nums:
            if i - x > k:
                count += 1
                x = i

        return count
            