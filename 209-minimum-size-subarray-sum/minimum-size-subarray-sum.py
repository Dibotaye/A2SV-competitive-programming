class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        l = 0
        summ = 0
        for r in range(n):
            summ += nums[r]
            while summ >= target:
                min_len = min(min_len, r-l+1)
                summ -= nums[l]
                l += 1

        if min_len == float('inf'):
            return 0
        return min_len



