class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        ans = []
        for i in queries:
            max_size = 0
            for j in range(len(prefix)):
                if prefix[j] <= i:
                    max_size = j+1                
            ans.append(max_size)
        return ans


            